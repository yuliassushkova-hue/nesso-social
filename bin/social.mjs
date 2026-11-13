#!/usr/bin/env node
// nesso-social: one queue of posts, published on a schedule to Instagram, Threads, LinkedIn and YouTube.
//
// A post is a folder under posts/ holding post.md (front matter + caption) and its media.
// A post on main is approved: drafts live on branches and are approved by merging.
// published.json is the record of what went out, and the only thing that stops a post
// going out twice.
//
//   node bin/social.mjs check                  validate every unpublished post
//   node bin/social.mjs list                   the schedule, with each post's state
//   node bin/social.mjs publish [--dry-run]    publish what is due
//   node bin/social.mjs whoami                 which account each token reaches
//   node bin/social.mjs refresh-tokens         refresh the tokens into GitHub secrets
//   node bin/social.mjs exchange-threads NAME  short-lived Threads token -> long-lived secret NAME
//   node bin/social.mjs linkedin-login CHANNEL sign a LinkedIn channel in, on this Mac (every 60 days)
//   node bin/social.mjs linkedin-expiry        open an issue when a LinkedIn sign-in is about to lapse
//   node bin/social.mjs youtube-login CHANNEL  sign a YouTube channel in, on this Mac (once)
//
// Every Instagram Reel also goes to the YouTube channel of its language as a Short, at the same
// time: the YouTube post is derived from the Instagram one and has no folder of its own.

import { readFileSync, readdirSync, existsSync, writeFileSync, statSync } from 'node:fs';
import { join, extname, basename, dirname, resolve, relative, sep } from 'node:path';
import { execFileSync } from 'node:child_process';
import { createHash, randomBytes } from 'node:crypto';
import { createServer } from 'node:http';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const POSTS = resolve(process.env.POSTS_DIR ?? join(ROOT, 'posts'));
const LOG = resolve(process.env.PUBLISHED_LOG ?? join(ROOT, 'published.json'));

const IG = 'https://graph.instagram.com/v23.0';
const FB = 'https://graph.facebook.com/v23.0';
const THREADS = 'https://graph.threads.net/v1.0';
const LI = 'https://api.linkedin.com';
const LI_OAUTH = 'https://www.linkedin.com/oauth/v2';
// Every /rest call names the month of the API it was written against. LinkedIn keeps a version for
// about a year, then refuses it: move this forward before then (Microsoft Learn, "Posts API").
const LI_VERSION = '202610';

// A post this many hours past its time is not published late: it is reported and skipped.
const MAX_LATE_HOURS = 36;

// `account` names an optional variable holding the Instagram account id, for a Facebook-format
// token whose account cannot be found by asking the API (see igAccount).
export const CHANNELS = {
  'ig-it': { platform: 'instagram', token: 'IG_IT_TOKEN', account: 'IG_IT_ACCOUNT_ID' },
  'ig-dk': { platform: 'instagram', token: 'IG_DK_TOKEN', account: 'IG_DK_ACCOUNT_ID' },
  'ig-en': { platform: 'instagram', token: 'IG_EN_TOKEN', account: 'IG_EN_ACCOUNT_ID' },
  'threads-it': { platform: 'threads', token: 'THREADS_IT_TOKEN' },
  'threads-dk': { platform: 'threads', token: 'THREADS_DK_TOKEN' },
  // A person posts as themselves with the self-serve Share on LinkedIn product; the profile is
  // found from the token. A Page needs the Community Management API, which LinkedIn approves for an
  // app of its own, and the Page's organization id in accounts.json.
  'li-julia': { platform: 'linkedin', token: 'LI_JULIA_TOKEN', scope: 'openid profile w_member_social' },
  'li-nesso': { platform: 'linkedin', token: 'LI_NESSO_TOKEN', account: 'LI_NESSO_ORG_ID', scope: 'w_organization_social' },
  // The token is the channel's refresh token; YT_CLIENT_ID and YT_CLIENT_SECRET are the one Google app.
  'yt-it': { platform: 'youtube', token: 'YT_IT_TOKEN', mirrors: 'ig-it', lang: 'it', link: 'https://nesso.fit/it?via=youtube' },
  'yt-en': { platform: 'youtube', token: 'YT_EN_TOKEN', mirrors: 'ig-en', lang: 'en', link: 'https://nesso.fit/?via=youtube' },
  'yt-dk': { platform: 'youtube', token: 'YT_DK_TOKEN', mirrors: 'ig-dk', lang: 'da', link: 'https://nesso.fit/da?via=youtube' },
};

// What each platform accepts, from its own content-publishing docs.
const RULES = {
  instagram: {
    types: { image: [1, 1], carousel: [2, 10], reel: [1, 1], story: [1, 1] },
    images: ['.jpg', '.jpeg'], // Instagram's publishing API takes JPEG only
    videos: ['.mp4', '.mov'],
    captionMax: 2200,
    hashtagMax: 30,
  },
  threads: {
    types: { text: [0, 0], image: [1, 1], video: [1, 1], carousel: [2, 20] },
    images: ['.jpg', '.jpeg', '.png'],
    videos: ['.mp4', '.mov'],
    captionMax: 500,
    hashtagMax: Infinity,
  },
  youtube: {
    types: { reel: [1, 1] }, // a vertical video under three minutes is a Short
    images: [],
    videos: ['.mp4', '.mov'],
    captionMax: 5000, // the description, in bytes; counted as characters here, which is stricter for ASCII only
    hashtagMax: 60, // above 60 YouTube ignores every hashtag on the video
  },
  linkedin: {
    types: { text: [0, 0], image: [1, 1], 'multi-image': [2, 20] },
    images: ['.jpg', '.jpeg', '.png'],
    videos: [],
    captionMax: 3000, // counted after escaping, which is what LinkedIn stores
    hashtagMax: Infinity,
  },
};

const MIME = { '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.mp4': 'video/mp4', '.mov': 'video/quicktime' };

// ---------------------------------------------------------------- the queue

export function parsePost(dir) {
  const id = basename(dir);
  const raw = readFileSync(join(dir, 'post.md'), 'utf8').replace(/\r\n/g, '\n');
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return { id, dir, errors: ['post.md must start with a --- front matter block'] };
  const meta = {};
  for (const line of m[1].split('\n')) {
    const text = line.replace(/\s+#\s.*$/, '').trim();
    if (!text) continue;
    const i = text.indexOf(':');
    if (i < 0) continue;
    meta[text.slice(0, i).trim()] = text.slice(i + 1).trim();
  }
  return {
    id,
    dir,
    channel: meta.channel,
    at: meta.at,
    type: meta.type,
    media: (meta.media ?? '').split(',').map((s) => s.trim()).filter(Boolean),
    caption: m[2].trim(),
  };
}

export function validate(post) {
  const errors = [...(post.errors ?? [])];
  if (errors.length) return errors;
  const channel = CHANNELS[post.channel];
  if (!channel) return [`channel must be one of ${Object.keys(CHANNELS).join(', ')}`];
  const rules = RULES[channel.platform];
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})$/.test(post.at ?? '')) {
    errors.push('at must be a time with its offset, e.g. 2026-11-04T18:00+01:00');
  }
  const range = rules.types[post.type];
  if (!range) {
    errors.push(`type on ${channel.platform} must be one of ${Object.keys(rules.types).join(', ')}`);
  } else if (post.media.length < range[0] || post.media.length > range[1]) {
    errors.push(`a ${post.type} takes ${range[0] === range[1] ? range[0] : `${range[0]} to ${range[1]}`} media file(s), got ${post.media.length}`);
  }
  for (const name of post.media) {
    const ext = extname(name).toLowerCase();
    if (!existsSync(join(post.dir, name))) errors.push(`media file not found: ${name}`);
    const isImage = rules.images.includes(ext);
    const isVideo = rules.videos.includes(ext);
    if (!isImage && !isVideo) errors.push(`${name}: ${channel.platform} takes ${[...rules.images, ...rules.videos].join(' ')}`);
    if (post.type === 'image' && !isImage) errors.push(`${name}: an image post needs an image`);
    if ((post.type === 'reel' || post.type === 'video') && !isVideo) errors.push(`${name}: a ${post.type} needs a video`);
  }
  if (post.type === 'story' && post.caption) errors.push('a story carries no caption: leave the body empty');
  if (post.type === 'text' && !post.caption) errors.push('a text post needs text');
  const sent = channel.platform === 'linkedin' ? littleText(post.caption) : post.caption;
  if (sent.length > rules.captionMax) errors.push(`caption is ${sent.length} characters, ${channel.platform} takes ${rules.captionMax}`);
  const tags = post.caption.match(/(^|\s)#[\p{L}\p{N}_]+/gu) ?? [];
  if (tags.length > rules.hashtagMax) errors.push(`${tags.length} hashtags, ${channel.platform} takes ${rules.hashtagMax}`);
  return errors;
}

function readPosts() {
  if (!existsSync(POSTS)) return [];
  const posts = readdirSync(POSTS)
    .map((name) => join(POSTS, name))
    .filter((dir) => statSync(dir).isDirectory() && existsSync(join(dir, 'post.md')))
    .map(parsePost);
  return [...posts, ...posts.flatMap(mirrorsOf)].sort((a, b) => Date.parse(a.at) - Date.parse(b.at) || a.id.localeCompare(b.id));
}

// ---------------------------------------------------------------- YouTube Shorts from Reels

// Reels before this were made for Instagram only; YouTube copies start here (founder, 13 November).
const YOUTUBE_FROM = Date.parse('2026-11-13T00:00+01:00');

export function mirrorsOf(post) {
  if (post.type !== 'reel' || post.errors || !(Date.parse(post.at) >= YOUTUBE_FROM)) return [];
  return Object.entries(CHANNELS)
    .filter(([, channel]) => channel.mirrors === post.channel)
    .map(([name, channel]) => ({ ...post, id: `${post.id}~${name}`, channel: name, caption: youtubeDescription(post.caption, channel.link), mirror: true }));
}

// Instagram says "link in bio"; on YouTube the link goes in the description itself.
export function youtubeDescription(caption, link) {
  return caption.replace(/link (in|i) bio\.?/giu, link).replace(/[<>]/g, '');
}

// The title is the caption's first sentence, cut at a word to YouTube's 100 characters.
export function youtubeTitle(caption) {
  const first = caption.split('\n').map((l) => l.trim()).find(Boolean)?.replace(/[<>]/g, '') ?? 'Nesso';
  const sentence = first.match(/^.+?[.!?»"](?=\s|$)/u)?.[0] ?? first;
  const title = sentence.length <= 100 ? sentence : first;
  if (title.length <= 100) return title;
  return `${title.slice(0, 99).replace(/\s+\S*$/u, '')}…`;
}

// Instagram account ids are not secrets, so they live in the repository: accounts.json maps a
// channel to the id Meta shows beside the account under "Generate access tokens".
const ACCOUNTS = join(ROOT, 'accounts.json');
const accountIdFor = (name) =>
  process.env[CHANNELS[name].account] || (existsSync(ACCOUNTS) ? JSON.parse(readFileSync(ACCOUNTS, 'utf8'))[name] : undefined);

const readLog = () => (existsSync(LOG) ? JSON.parse(readFileSync(LOG, 'utf8')) : {});
const writeLog = (log) => writeFileSync(LOG, `${JSON.stringify(log, null, 2)}\n`);

export function stateOf(post, log, now = Date.now()) {
  if (log[post.id]) return 'published';
  const at = Date.parse(post.at);
  if (Number.isNaN(at)) return 'invalid';
  if (at > now) return 'scheduled';
  if (now - at > MAX_LATE_HOURS * 3600_000) return 'missed';
  return 'due';
}

// ---------------------------------------------------------------- the APIs

async function api(method, url, params) {
  const u = new URL(url);
  let body;
  if (method === 'GET') for (const [k, v] of Object.entries(params)) u.searchParams.set(k, String(v));
  else body = new URLSearchParams(Object.entries(params).map(([k, v]) => [k, String(v)]));
  const res = await fetch(u, { method, body });
  const json = await res.json().catch(() => ({}));
  // The token rides in the parameters, so only the path is ever printed.
  if (!res.ok || json.error) throw new Error(`${method} ${u.host}${u.pathname}: ${json.error?.message ?? `HTTP ${res.status}`}`);
  return json;
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitReady(base, id, token, field) {
  for (let i = 0; i < 60; i++) {
    const s = await api('GET', `${base}/${id}`, { fields: field === 'status' ? 'status,error_message' : 'status_code', access_token: token });
    const status = s[field];
    if (status === 'FINISHED') return;
    if (status === 'ERROR' || status === 'EXPIRED') throw new Error(`container ${id} ${status}${s.error_message ? `: ${s.error_message}` : ''}`);
    await sleep(10_000);
  }
  throw new Error(`container ${id} not ready after ten minutes`);
}

const isVideo = (url) => ['.mp4', '.mov'].includes(extname(new URL(url).pathname).toLowerCase());

// Meta hands out two kinds of Instagram token. One from Instagram Login (IGAA…) talks to
// graph.instagram.com and /me is the account. One from Facebook Login for Business or a
// system user (EAA…) talks to graph.facebook.com, where /me is a person or a system user and
// the Instagram account has to be found through what that token can reach.
async function igAccount(token, accountId) {
  if (token.startsWith('IG')) {
    const me = await api('GET', `${IG}/me`, { fields: 'user_id,username', access_token: token });
    return { base: IG, id: me.user_id ?? me.id, username: me.username };
  }
  if (accountId) {
    try {
      const account = await api('GET', `${FB}/${accountId}`, { fields: 'id,username', access_token: token });
      return { base: FB, id: account.id, username: account.username };
    } catch (error) {
      // Say what kind of object the id is, so the right id can be found from it.
      const meta = await api('GET', `${FB}/${accountId}`, { metadata: 1, access_token: token }).catch((e) => ({ error: e.message }));
      const fields = (meta.metadata?.fields ?? []).map((f) => f.name).join(',');
      const edges = Object.keys(meta.metadata?.connections ?? {}).join(',');
      throw new Error(`${error.message} | type ${meta.metadata?.type} | fields ${fields} | edges ${edges} | ${JSON.stringify(Object.fromEntries(Object.entries(meta).filter(([k]) => k !== 'metadata')))}`);
    }
  }
  const tried = [];
  const attempt = async (label, fn) => {
    try {
      return await fn();
    } catch (error) {
      tried.push(`${label}: ${error.message}`);
      return null;
    }
  };
  // A Unified Login token may also be accepted by graph.instagram.com, where /me is the account.
  const viaInstagram = await attempt('graph.instagram.com/me', async () => {
    const me = await api('GET', `${IG}/me`, { fields: 'user_id,username', access_token: token });
    return { base: IG, id: me.user_id ?? me.id, username: me.username };
  });
  if (viaInstagram) return viaInstagram;
  // Through a Facebook Page the account is linked to.
  const viaPages = await attempt('me/accounts', async () => {
    const pages = await api('GET', `${FB}/me/accounts`, { fields: 'instagram_business_account{id,username}', access_token: token });
    const linked = (pages.data ?? []).map((p) => p.instagram_business_account).filter(Boolean);
    if (linked.length !== 1) throw new Error(`${linked.length} Instagram accounts`);
    return { base: FB, id: linked[0].id, username: linked[0].username };
  });
  if (viaPages) return viaPages;
  // Through the business portfolio that owns it.
  const viaBusiness = await attempt('me/businesses', async () => {
    const businesses = await api('GET', `${FB}/me/businesses`, { fields: 'id', access_token: token });
    const found = [];
    for (const b of businesses.data ?? []) {
      for (const edge of ['owned_instagram_accounts', 'instagram_accounts']) {
        const list = await api('GET', `${FB}/${b.id}/${edge}`, { fields: 'id,username', access_token: token }).catch(() => ({}));
        for (const a of list.data ?? []) if (!found.some((f) => f.id === a.id)) found.push(a);
      }
    }
    if (found.length !== 1) throw new Error(`${found.length} Instagram accounts (${found.map((a) => `@${a.username} ${a.id}`).join(', ')})`);
    return { base: FB, id: found[0].id, username: found[0].username };
  });
  if (viaBusiness) return viaBusiness;
  // Nothing found: say at least who the token belongs to.
  await attempt('me', async () => {
    const me = await api('GET', `${FB}/me`, { fields: 'id,name', access_token: token });
    tried.push(`token belongs to "${me.name}" (${me.id})`);
  });
  throw new Error(`could not find the Instagram account for this token (${tried.join('; ')}); set its account id`);
}

async function whoIs(platform, token, accountId, name) {
  if (platform === 'instagram') return igAccount(token, accountId);
  if (platform === 'youtube') return youtubeChannel(await googleAccess(token));
  if (platform === 'linkedin') {
    const author = await linkedinAuthor(name, token);
    return { id: author.urn, username: author.label };
  }
  const me = await api('GET', `${THREADS}/me`, { fields: 'id,username', access_token: token });
  return { id: me.id, username: me.username };
}

// Builds the platform's container for a post and waits until the platform has fetched and
// processed every file. Nothing is visible until the container is published, so a rehearsal can
// stop here: an unpublished container expires on its own after a day.
async function prepareInstagram(post, token, urls, accountId) {
  const me = await igAccount(token, accountId);
  const IG = me.base; // the rest of this function speaks to whichever host the token belongs to
  const create = (params) => api('POST', `${IG}/${me.id}/media`, { ...params, access_token: token });
  const mediaParams = (url) => (isVideo(url) ? { media_type: 'VIDEO', video_url: url } : { image_url: url });
  let container;
  if (post.type === 'image') container = await create({ image_url: urls[0], caption: post.caption });
  if (post.type === 'reel') container = await create({ media_type: 'REELS', video_url: urls[0], caption: post.caption });
  if (post.type === 'story') {
    container = await create(isVideo(urls[0]) ? { media_type: 'STORIES', video_url: urls[0] } : { media_type: 'STORIES', image_url: urls[0] });
  }
  if (post.type === 'carousel') {
    const children = [];
    for (const url of urls) {
      const child = await create({ ...mediaParams(url), is_carousel_item: true });
      await waitReady(IG, child.id, token, 'status_code');
      children.push(child.id);
    }
    container = await create({ media_type: 'CAROUSEL', children: children.join(','), caption: post.caption });
  }
  await waitReady(IG, container.id, token, 'status_code');
  return { me, container };
}

async function publishInstagram(post, token, urls, accountId) {
  const { me, container } = await prepareInstagram(post, token, urls, accountId);
  const published = await api('POST', `${me.base}/${me.id}/media_publish`, { creation_id: container.id, access_token: token });
  const info = await api('GET', `${me.base}/${published.id}`, { fields: 'permalink', access_token: token }).catch(() => ({}));
  return { mediaId: published.id, permalink: info.permalink ?? null, account: me.username };
}

async function prepareThreads(post, token, urls) {
  const me = await whoIs('threads', token);
  const create = (params) => api('POST', `${THREADS}/${me.id}/threads`, { ...params, access_token: token });
  const mediaParams = (url) => (isVideo(url) ? { media_type: 'VIDEO', video_url: url } : { media_type: 'IMAGE', image_url: url });
  let container;
  if (post.type === 'text') container = await create({ media_type: 'TEXT', text: post.caption });
  if (post.type === 'image' || post.type === 'video') container = await create({ ...mediaParams(urls[0]), text: post.caption });
  if (post.type === 'carousel') {
    const children = [];
    for (const url of urls) {
      const child = await create({ ...mediaParams(url), is_carousel_item: true });
      await waitReady(THREADS, child.id, token, 'status');
      children.push(child.id);
    }
    container = await create({ media_type: 'CAROUSEL', children: children.join(','), text: post.caption });
  }
  await waitReady(THREADS, container.id, token, 'status');
  return { me, container };
}

async function publishThreads(post, token, urls) {
  const { me, container } = await prepareThreads(post, token, urls);
  const published = await api('POST', `${THREADS}/${me.id}/threads_publish`, { creation_id: container.id, access_token: token });
  const info = await api('GET', `${THREADS}/${published.id}`, { fields: 'permalink', access_token: token }).catch(() => ({}));
  return { mediaId: published.id, permalink: info.permalink ?? null, account: me.username };
}

// LinkedIn reads a post's text as "little" markup, where | { } @ [ ] ( ) < > # \ * _ ~ mean
// something, and a bare one can cut the post off where it stands. Every one is escaped except a #
// that starts a hashtag, so #housing still becomes a hashtag.
export function littleText(text) {
  return text.replace(/[\\|{}@[\]()<>#*_~]/g, (ch, i, s) =>
    ch === '#' && (i === 0 || /\s/.test(s[i - 1])) && /[\p{L}\p{N}_]/u.test(s[i + 1] ?? '') ? ch : `\\${ch}`,
  );
}

async function liApi(method, path, token, body) {
  const headers = { Authorization: `Bearer ${token}` };
  if (path.startsWith('/rest/')) Object.assign(headers, { 'LinkedIn-Version': LI_VERSION, 'X-Restli-Protocol-Version': '2.0.0' });
  if (body) headers['Content-Type'] = 'application/json';
  const res = await fetch(`${LI}${path}`, { method, headers, body: body ? JSON.stringify(body) : undefined });
  const json = await res.json().catch(() => ({}));
  if (!res.ok) {
    const hint = res.status === 401 ? ' (the sign-in has lapsed or was revoked: run linkedin-login again)' : '';
    const error = new Error(`${method} api.linkedin.com${path.split('?')[0]}: ${json.message ?? `HTTP ${res.status}`}${hint}`);
    error.status = res.status;
    throw error;
  }
  return { json, id: res.headers.get('x-restli-id') };
}

// Who a LinkedIn channel posts as. A Page is named by its id; a person is whoever the token
// belongs to, so the token cannot post to a profile it was not issued for.
async function linkedinAuthor(name, token) {
  if (CHANNELS[name].account) {
    const org = accountIdFor(name);
    if (!org) throw new Error(`${name} needs its organization id in accounts.json`);
    return { urn: `urn:li:organization:${org}`, label: `page ${org}` };
  }
  const { json: me } = await liApi('GET', '/v2/userinfo', token);
  return { urn: `urn:li:person:${me.sub}`, label: me.name ?? me.sub };
}

// LinkedIn takes the file itself rather than a link to it, so nothing here needs a public URL.
async function uploadLinkedInImage(post, name, owner, token) {
  const { json } = await liApi('POST', '/rest/images?action=initializeUpload', token, { initializeUploadRequest: { owner } });
  const { uploadUrl, image } = json.value ?? {};
  if (!uploadUrl || !image) throw new Error(`LinkedIn gave no upload address for ${name}`);
  const res = await fetch(uploadUrl, {
    method: 'PUT',
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/octet-stream' },
    body: readFileSync(join(post.dir, name)),
  });
  if (!res.ok) throw new Error(`uploading ${name} to LinkedIn: HTTP ${res.status}`);
  return image;
}

// LinkedIn has no unpublished container, so a rehearsal stops after this: the token works and
// every image was accepted. An uploaded image no post uses is never shown.
async function prepareLinkedIn(post, token) {
  const author = await linkedinAuthor(post.channel, token);
  const images = [];
  for (const name of post.media) images.push(await uploadLinkedInImage(post, name, author.urn, token));
  return { author, images };
}

async function publishLinkedIn(post, token) {
  const { author, images } = await prepareLinkedIn(post, token);
  const body = {
    author: author.urn,
    commentary: littleText(post.caption),
    visibility: 'PUBLIC',
    distribution: { feedDistribution: 'MAIN_FEED', targetEntities: [], thirdPartyDistributionChannels: [] },
    lifecycleState: 'PUBLISHED',
    isReshareDisabledByAuthor: false,
  };
  if (images.length === 1) body.content = { media: { id: images[0] } };
  if (images.length > 1) body.content = { multiImage: { images: images.map((id) => ({ id })) } };
  // An image uploaded a moment ago can still be processing. A post refused with 400 or 422 was not
  // created, so asking again is safe; nothing else is retried here, so a post never goes out twice.
  let created;
  for (let attempt = 1; !created; attempt++) {
    try {
      created = await liApi('POST', '/rest/posts', token, body);
    } catch (error) {
      if (!images.length || attempt === 3 || ![400, 422].includes(error.status)) throw error;
      await sleep(15_000);
    }
  }
  return { mediaId: created.id, permalink: created.id ? `https://www.linkedin.com/feed/update/${created.id}/` : null, account: author.label };
}

// YouTube takes the file itself, in a resumable upload: a session URL first, then the bytes.
const GOOGLE_TOKEN = 'https://oauth2.googleapis.com/token';
const YT = 'https://www.googleapis.com/youtube/v3';

async function googleAccess(refreshToken) {
  const { YT_CLIENT_ID: clientId, YT_CLIENT_SECRET: secret } = process.env;
  if (!clientId || !secret) throw new Error('YT_CLIENT_ID and YT_CLIENT_SECRET are not set');
  const res = await fetch(GOOGLE_TOKEN, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ client_id: clientId, client_secret: secret, refresh_token: refreshToken, grant_type: 'refresh_token' }),
  });
  const answer = await res.json().catch(() => ({}));
  if (!res.ok || !answer.access_token) throw new Error(`Google refused the sign-in: ${answer.error_description ?? answer.error ?? `HTTP ${res.status}`}`);
  return answer.access_token;
}

async function googleError(res) {
  const body = await res.json().catch(() => ({}));
  return new Error(`YouTube answered HTTP ${res.status}: ${body.error?.message ?? 'no message'}`);
}

async function youtubeChannel(access) {
  const res = await fetch(`${YT}/channels?part=snippet&mine=true`, { headers: { Authorization: `Bearer ${access}` } });
  if (!res.ok) throw await googleError(res);
  const channel = (await res.json()).items?.[0];
  if (!channel) throw new Error('this Google sign-in has no YouTube channel');
  return { username: channel.snippet.title, id: channel.id };
}

async function publishYouTube(post, refreshToken) {
  const access = await googleAccess(refreshToken);
  const channel = CHANNELS[post.channel];
  const file = join(post.dir, post.media[0]);
  const bytes = readFileSync(file);
  const type = MIME[extname(file).toLowerCase()];
  const meta = {
    snippet: { title: youtubeTitle(post.caption), description: post.caption, categoryId: '26', defaultLanguage: channel.lang, defaultAudioLanguage: channel.lang },
    // Stock footage and drawn cards: nothing realistic is made up, so nothing to disclose.
    status: { privacyStatus: 'public', selfDeclaredMadeForKids: false, containsSyntheticMedia: false },
  };
  const start = await fetch('https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status', {
    method: 'POST',
    headers: { Authorization: `Bearer ${access}`, 'Content-Type': 'application/json; charset=UTF-8', 'X-Upload-Content-Type': type, 'X-Upload-Content-Length': String(bytes.length) },
    body: JSON.stringify(meta),
  });
  if (!start.ok) throw await googleError(start);
  const upload = await fetch(start.headers.get('location'), { method: 'PUT', headers: { 'Content-Type': type, 'Content-Length': String(bytes.length) }, body: bytes });
  if (!upload.ok) throw await googleError(upload);
  const video = await upload.json();
  const me = await youtubeChannel(access).catch(() => ({ username: post.channel }));
  return { mediaId: video.id, permalink: `https://www.youtube.com/shorts/${video.id}`, account: me.username };
}

// Both APIs fetch media from a public URL. The repository is public, so in Actions a file is
// served straight from GitHub at the exact commit being published. An R2 bucket, when its
// variables are set, is used instead (for a private repository).
async function mediaUrl(post, name) {
  if (process.env.R2_BUCKET) return uploadMedia(post, name);
  const repo = process.env.GITHUB_REPOSITORY;
  const sha = process.env.MEDIA_SHA || process.env.GITHUB_SHA; // a pull request runs on a merge commit; its files are at the head
  if (!repo || !sha) throw new Error('media needs either the R2 variables or a GitHub Actions run');
  const path = relative(ROOT, join(post.dir, name)).split(sep).map(encodeURIComponent).join('/');
  const url = `https://raw.githubusercontent.com/${repo}/${sha}/${path}`;
  const res = await fetch(url, { method: 'HEAD' });
  if (!res.ok) throw new Error(`${name} is not reachable at ${url} (HTTP ${res.status}); is the repository public?`);
  return url;
}

function uploadMedia(post, name) {
  const file = join(post.dir, name);
  const digest = createHash('sha256').update(readFileSync(file)).digest('hex').slice(0, 12);
  const key = `${post.id}/${digest}${extname(name).toLowerCase()}`;
  const need = ['R2_ACCOUNT_ID', 'R2_ACCESS_KEY_ID', 'R2_SECRET_ACCESS_KEY', 'R2_BUCKET', 'MEDIA_BASE_URL'].filter((k) => !process.env[k]);
  if (need.length) throw new Error(`media upload needs ${need.join(', ')}`);
  execFileSync(
    'aws',
    ['s3', 'cp', file, `s3://${process.env.R2_BUCKET}/${key}`, '--endpoint-url', `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com`, '--content-type', MIME[extname(name).toLowerCase()], '--only-show-errors'],
    {
      stdio: 'inherit',
      env: {
        ...process.env,
        AWS_ACCESS_KEY_ID: process.env.R2_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY: process.env.R2_SECRET_ACCESS_KEY,
        AWS_DEFAULT_REGION: 'auto',
        AWS_REQUEST_CHECKSUM_CALCULATION: 'when_required',
        AWS_RESPONSE_CHECKSUM_VALIDATION: 'when_required',
      },
    },
  );
  return `${process.env.MEDIA_BASE_URL.replace(/\/$/, '')}/${key}`;
}

// ---------------------------------------------------------------- commands

function check() {
  const log = readLog();
  let failed = 0;
  for (const post of readPosts()) {
    if (log[post.id]) continue;
    const errors = validate(post);
    const state = stateOf(post, log);
    if (errors.length) {
      failed++;
      console.log(`✗ ${post.id}`);
      for (const e of errors) console.log(`    ${e}`);
    } else {
      console.log(`✓ ${post.id}  ${post.channel}  ${post.at}${state === 'scheduled' ? '' : `  (${state})`}`);
    }
  }
  if (failed) process.exitCode = 1;
}

function list() {
  const log = readLog();
  for (const post of readPosts()) {
    const state = stateOf(post, log);
    const extra = state === 'published' ? `  ${log[post.id].permalink ?? ''}` : '';
    console.log(`${state.padEnd(9)}  ${String(post.at).padEnd(25)}  ${String(post.channel).padEnd(10)}  ${post.id}${extra}`);
  }
}

async function publish({ dryRun }) {
  const log = readLog();
  let failed = 0;
  for (const post of readPosts()) {
    const state = stateOf(post, log);
    if (post.mirror && !process.env[CHANNELS[post.channel].token]) continue; // the channel is not signed in yet
    if (state === 'missed' && !log[post.id] && !post.mirror) console.log(`! ${post.id} is more than ${MAX_LATE_HOURS}h past its time and was not published; move its time to publish it`);
    if (state !== 'due') continue;
    const errors = validate(post);
    if (errors.length) {
      failed++;
      console.log(`✗ ${post.id}: ${errors.join('; ')}`);
      continue;
    }
    const channel = CHANNELS[post.channel];
    if (dryRun) {
      console.log(`would publish ${post.id} to ${post.channel} (${post.type}, ${post.media.length} media)`);
      continue;
    }
    try {
      const token = process.env[channel.token];
      if (!token) throw new Error(`secret ${channel.token} is not set`);
      const urls = [];
      if (!['linkedin', 'youtube'].includes(channel.platform)) for (const name of post.media) urls.push(await mediaUrl(post, name));
      const result =
        channel.platform === 'instagram'
          ? await publishInstagram(post, token, urls, accountIdFor(post.channel))
          : channel.platform === 'linkedin'
            ? await publishLinkedIn(post, token)
            : channel.platform === 'youtube'
              ? await publishYouTube(post, token)
              : await publishThreads(post, token, urls);
      log[post.id] = { channel: post.channel, at: post.at, publishedAt: new Date().toISOString(), ...result };
      writeLog(log); // after each post, so a later failure cannot cause a repeat
      console.log(`✓ ${post.id} → @${result.account} ${result.permalink ?? result.mediaId}`);
    } catch (error) {
      failed++;
      console.log(`✗ ${post.id}: ${error.message}`);
    }
  }
  if (failed) process.exitCode = 1;
}

// Every post not yet published, whatever its time: the platform fetches and processes each file
// exactly as it will on the day, and nothing is published. Run on a week's branch before it is
// merged, so a video Instagram refuses is found while there is time to fix it.
async function rehearse() {
  const log = readLog();
  // Only the posts a pull request adds or changes, named by the workflow: every rehearsal creates a
  // container per post, and rehearsing a whole week several times a day trips Instagram's
  // "too many actions" limit, which then blocks real publishing too.
  const only = (process.env.REHEARSE_ONLY ?? '').split(',').map((s) => s.trim()).filter(Boolean);
  const posts = readPosts().filter((post) => !log[post.id] && only.includes(post.id));
  if (!posts.length) {
    console.log('nothing to rehearse: no new or changed posts');
    return;
  }
  let failed = 0;
  const one = async (post) => {
    const errors = validate(post);
    if (errors.length) throw new Error(errors.join('; '));
    const channel = CHANNELS[post.channel];
    const token = process.env[channel.token];
    if (!token) throw new Error(`secret ${channel.token} is not set`);
    if (channel.platform === 'linkedin') return prepareLinkedIn(post, token);
    const urls = [];
    for (const name of post.media) urls.push(await mediaUrl(post, name));
    if (channel.platform === 'instagram') await prepareInstagram(post, token, urls, accountIdFor(post.channel));
    else await prepareThreads(post, token, urls);
  };
  const queue = [...posts];
  const worker = async () => {
    for (let post = queue.shift(); post; post = queue.shift()) {
      try {
        await one(post);
        console.log(`✓ ${post.id}  accepted, not published`);
      } catch (error) {
        failed++;
        console.log(`✗ ${post.id}: ${error.message}`);
      }
    }
  };
  await worker(); // one at a time, gently
  console.log(`${posts.length - failed} of ${posts.length} posts would be accepted`);
  if (failed) process.exitCode = 1;
}

async function whoami() {
  for (const [name, channel] of Object.entries(CHANNELS)) {
    const token = process.env[channel.token];
    if (!token) {
      console.log(`${name.padEnd(10)}  no ${channel.token}`);
      continue;
    }
    try {
      const me = await whoIs(channel.platform, token, accountIdFor(name), name);
      console.log(`${name.padEnd(10)}  @${me.username}  (account id ${me.id})`);
    } catch (error) {
      process.exitCode = 1;
      console.log(`${name.padEnd(10)}  ✗ ${error.message}`);
    }
  }
}

// gh refuses secret and variable commands in a checkout with more than one remote unless the
// repository is named, so every gh call names it: Actions says which, and on a Mac it is origin's.
function ghRepo() {
  if (process.env.GITHUB_REPOSITORY) return process.env.GITHUB_REPOSITORY;
  const origin = execFileSync('git', ['remote', 'get-url', 'origin'], { encoding: 'utf8' }).trim();
  return origin.replace(/^.*github\.com[:/]/, '').replace(/\.git$/, '');
}

function setSecret(name, value) {
  execFileSync('gh', ['secret', 'set', name, '--repo', ghRepo()], { input: value, stdio: ['pipe', 'inherit', 'inherit'] });
}

async function refreshTokens() {
  for (const channel of Object.values(CHANNELS)) {
    const token = process.env[channel.token];
    if (!token) continue;
    if (channel.platform === 'linkedin') {
      console.log(`- ${channel.token}: LinkedIn gives this kind of app no refresh; run linkedin-login before it lapses`);
      continue;
    }
    if (channel.platform === 'youtube') {
      console.log(`- ${channel.token} is a Google refresh token: it does not expire while the app is in production`);
      continue;
    }
    // A Facebook-format token from a system user does not expire and has no refresh call.
    if (channel.platform === 'instagram' && !token.startsWith('IG')) {
      console.log(`- ${channel.token} is a Facebook-format token: nothing to refresh`);
      continue;
    }
    try {
      const fresh =
        channel.platform === 'instagram'
          ? await api('GET', 'https://graph.instagram.com/refresh_access_token', { grant_type: 'ig_refresh_token', access_token: token })
          : await api('GET', 'https://graph.threads.net/refresh_access_token', { grant_type: 'th_refresh_token', access_token: token });
      setSecret(channel.token, fresh.access_token);
      console.log(`✓ ${channel.token} refreshed, good for ${Math.round(fresh.expires_in / 86400)} days`);
    } catch (error) {
      process.exitCode = 1;
      console.log(`✗ ${channel.token}: ${error.message}`);
    }
  }
}

async function exchangeThreads(name) {
  if (!['THREADS_IT_TOKEN', 'THREADS_DK_TOKEN'].includes(name)) throw new Error('name must be THREADS_IT_TOKEN or THREADS_DK_TOKEN');
  const { THREADS_APP_SECRET: secret, SHORT_TOKEN: short } = process.env;
  if (!secret || !short) throw new Error('set THREADS_APP_SECRET and SHORT_TOKEN in the environment first (read -s, never on the command line)');
  const long = await api('GET', 'https://graph.threads.net/access_token', { grant_type: 'th_exchange_token', client_secret: secret, access_token: short });
  const me = await whoIs('threads', long.access_token);
  setSecret(name, long.access_token);
  console.log(`✓ ${name} set for @${me.username}, good for ${Math.round(long.expires_in / 86400)} days`);
}

// LinkedIn gives a self-serve app no refresh token: a sign-in lasts 60 days and is then made again.
// Run on this Mac. It opens LinkedIn's consent page, catches the answer on localhost (that address
// must be listed under the app's Auth tab exactly), and stores the token as the channel's secret and
// its last day as a repository variable, which linkedin-expiry watches. A token copied from the
// Developer Portal's Token Generator can be handed in as LI_TOKEN instead, and no browser opens.
const LI_REDIRECT = 'http://localhost:8765/linkedin';

function linkedinCode(clientId, scope) {
  const state = randomBytes(16).toString('hex');
  const url = new URL(`${LI_OAUTH}/authorization`);
  // Spaces between scopes as %20, the way LinkedIn's own examples write them, not as +.
  url.search = new URLSearchParams({ response_type: 'code', client_id: clientId, redirect_uri: LI_REDIRECT, state, scope }).toString().replace(/\+/g, '%20');
  const callback = new URL(LI_REDIRECT);
  return new Promise((done, fail) => {
    const server = createServer((req, res) => {
      const got = new URL(req.url, LI_REDIRECT);
      if (got.pathname !== callback.pathname) return res.writeHead(404).end();
      const code = got.searchParams.get('state') === state ? got.searchParams.get('code') : null;
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' }).end(code ? 'Done. You can close this tab.' : 'Not signed in. See the terminal.');
      server.close();
      if (code) done(code);
      else fail(new Error(`LinkedIn answered without a code: ${got.searchParams.get('error_description') ?? got.searchParams.get('error') ?? 'the state did not match'}`));
    });
    server.on('error', fail);
    // No host, so both IPv4 and IPv6 answer: a browser may ask for localhost over either. The
    // server takes one request and closes.
    server.listen(Number(callback.port), () => {
      console.log(`Opening LinkedIn. If no browser opens, go to:\n${url}`);
      try {
        execFileSync('open', [url.toString()]);
      } catch {}
    });
  });
}

async function linkedinLogin(name) {
  const channel = CHANNELS[name];
  const names = Object.keys(CHANNELS).filter((n) => CHANNELS[n].platform === 'linkedin');
  if (channel?.platform !== 'linkedin') throw new Error(`name a LinkedIn channel: ${names.join(', ')}`);
  let token = process.env.LI_TOKEN;
  let days = 60; // what LinkedIn issues today; the exchange below says so for itself
  if (!token) {
    const { LINKEDIN_CLIENT_ID: clientId, LINKEDIN_CLIENT_SECRET: secret } = process.env;
    if (!clientId || !secret) throw new Error('set LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET first (read -s, never on the command line), or LI_TOKEN from the Token Generator');
    const code = await linkedinCode(clientId, channel.scope);
    const res = await fetch(`${LI_OAUTH}/accessToken`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ grant_type: 'authorization_code', code, redirect_uri: LI_REDIRECT, client_id: clientId, client_secret: secret }),
    });
    const answer = await res.json().catch(() => ({}));
    if (!res.ok || !answer.access_token) throw new Error(`LinkedIn refused the code: ${answer.error_description ?? `HTTP ${res.status}`}`);
    token = answer.access_token;
    days = answer.expires_in / 86400;
  }
  const who = await linkedinAuthor(name, token); // fails here, before anything is stored, on a token that does not work
  const lastDay = new Date(Date.now() + days * 86400_000).toISOString().slice(0, 10);
  setSecret(channel.token, token);
  execFileSync('gh', ['variable', 'set', `${channel.token}_EXPIRES`, '--body', lastDay, '--repo', ghRepo()], { stdio: ['ignore', 'inherit', 'inherit'] });
  console.log(`✓ ${name} posts as ${who.label}; ${channel.token} works until ${lastDay}`);
}

// Run on this Mac, once per channel. Google's page asks which account and which channel; a Google
// account with several channels shows each. The answer comes back to this Mac on a loopback
// address, which a Desktop OAuth client accepts without registering it. Only the refresh token is
// kept, as the channel's secret, and it lasts while the app's consent screen is "In production".
const GOOGLE_REDIRECT = 'http://127.0.0.1:8766';

function googleCode(clientId) {
  const state = randomBytes(16).toString('hex');
  const url = new URL('https://accounts.google.com/o/oauth2/v2/auth');
  url.search = new URLSearchParams({
    client_id: clientId,
    redirect_uri: GOOGLE_REDIRECT,
    response_type: 'code',
    scope: 'https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.readonly',
    access_type: 'offline',
    prompt: 'consent select_account',
    state,
  }).toString();
  return new Promise((done, fail) => {
    const server = createServer((req, res) => {
      const got = new URL(req.url, GOOGLE_REDIRECT);
      if (got.pathname !== '/') return res.writeHead(404).end();
      const code = got.searchParams.get('state') === state ? got.searchParams.get('code') : null;
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' }).end(code ? 'Done. You can close this tab.' : 'Not signed in. See the terminal.');
      server.close();
      if (code) done(code);
      else fail(new Error(`Google answered without a code: ${got.searchParams.get('error') ?? 'the state did not match'}`));
    });
    server.on('error', fail);
    server.listen(8766, '127.0.0.1', () => {
      console.log(`Opening Google. If no browser opens, go to:\n${url}`);
      try {
        execFileSync('open', [url.toString()]);
      } catch {}
    });
  });
}

async function youtubeLogin(name) {
  const channel = CHANNELS[name];
  const names = Object.keys(CHANNELS).filter((n) => CHANNELS[n].platform === 'youtube');
  if (channel?.platform !== 'youtube') throw new Error(`name a YouTube channel: ${names.join(', ')}`);
  const { YT_CLIENT_ID: clientId, YT_CLIENT_SECRET: secret } = process.env;
  if (!clientId || !secret) throw new Error('set YT_CLIENT_ID and YT_CLIENT_SECRET first (read -s, never on the command line)');
  const code = await googleCode(clientId);
  const res = await fetch(GOOGLE_TOKEN, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ code, client_id: clientId, client_secret: secret, redirect_uri: GOOGLE_REDIRECT, grant_type: 'authorization_code' }),
  });
  const answer = await res.json().catch(() => ({}));
  if (!res.ok || !answer.refresh_token) throw new Error(`Google gave no refresh token: ${answer.error_description ?? answer.error ?? `HTTP ${res.status}`}`);
  const me = await youtubeChannel(answer.access_token); // fails here, before anything is stored, if the sign-in has no channel
  setSecret(channel.token, answer.refresh_token);
  console.log(`✓ ${name} uploads to the YouTube channel "${me.username}" (${me.id}); ${channel.token} is set`);
}

// Run weekly by Actions: an issue for each LinkedIn sign-in with ten days or fewer left, opened once.
const LI_WARN_DAYS = 10;

function linkedinExpiry(now = Date.now()) {
  for (const [name, channel] of Object.entries(CHANNELS)) {
    if (channel.platform !== 'linkedin') continue;
    const lastDay = process.env[`${channel.token}_EXPIRES`];
    if (!lastDay) {
      console.log(`${name.padEnd(10)}  not signed in`);
      continue;
    }
    const left = Math.floor((Date.parse(`${lastDay}T00:00:00Z`) - now) / 86400_000);
    console.log(`${name.padEnd(10)}  works until ${lastDay}, ${left} days left`);
    if (left > LI_WARN_DAYS) continue;
    const title = left < 0 ? `LinkedIn: ${name} is signed out since ${lastDay}` : `LinkedIn: sign ${name} in again before ${lastDay}`;
    const open = execFileSync('gh', ['issue', 'list', '--state', 'open', '--search', `"${title}" in:title`, '--json', 'title', '--repo', ghRepo()], { encoding: 'utf8' });
    if (JSON.parse(open).some((issue) => issue.title === title)) continue;
    const body = [
      left < 0
        ? `Вход в LinkedIn для \`${name}\` закончился ${lastDay}: посты в этот канал сейчас не выходят.`
        : `Вход в LinkedIn для \`${name}\` действует до ${lastDay}. После этого посты в этот канал не выходят.`,
      '',
      'Войти заново на Mac, в папке `nesso-social` (подробно в `SETUP.md` §6):',
      '',
      '```bash',
      'export LINKEDIN_CLIENT_ID=…   # вкладка Auth приложения',
      'read -s LINKEDIN_CLIENT_SECRET; export LINKEDIN_CLIENT_SECRET',
      `node bin/social.mjs linkedin-login ${name}`,
      'unset LINKEDIN_CLIENT_SECRET',
      '```',
    ].join('\n');
    execFileSync('gh', ['issue', 'create', '--title', title, '--body', body, '--repo', ghRepo()], { stdio: ['ignore', 'inherit', 'inherit'] });
  }
}

const [command, arg] = process.argv.slice(2);
const commands = {
  check,
  list,
  publish: () => publish({ dryRun: process.argv.includes('--dry-run') }),
  whoami,
  rehearse,
  'refresh-tokens': refreshTokens,
  'exchange-threads': () => exchangeThreads(arg),
  'linkedin-login': () => linkedinLogin(arg),
  'linkedin-expiry': () => linkedinExpiry(),
  'youtube-login': () => youtubeLogin(arg),
};
if (import.meta.url === `file://${process.argv[1]}` || process.argv[1]?.endsWith('social.mjs')) {
  if (!commands[command]) {
    console.log(`usage: node bin/social.mjs ${Object.keys(commands).join(' | ')}`);
    process.exitCode = 2;
  } else {
    await Promise.resolve(commands[command]()).catch((error) => {
      console.error(error.message);
      process.exitCode = 1;
    });
  }
}
