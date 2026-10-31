// One-off: what can the IG_IT_TOKEN read about the nesso_italia account? Prints shapes, never the token.
const T = process.env.IG_IT_TOKEN;
const ID = '1578760067137384';
const FB = 'https://graph.facebook.com/v23.0';
const get = async (label, url, params) => {
  const u = new URL(url);
  for (const [k, v] of Object.entries({ ...params, access_token: T })) u.searchParams.set(k, v);
  const r = await fetch(u);
  const j = await r.json().catch(() => ({}));
  console.log(`${label}: ${JSON.stringify(j.error ? { error: j.error.message } : j).slice(0, 400)}`);
};
await get('me', `${FB}/me`, {});
await get('me fields', `${FB}/me`, { fields: 'id,name' });
await get('id name', `${FB}/${ID}`, { fields: 'id,name' });
await get('id ig_id', `${FB}/${ID}`, { fields: 'ig_id' });
await get('id user_id', `${FB}/${ID}`, { fields: 'user_id' });
await get('id media', `${FB}/${ID}/media`, { limit: 1 });
await get('id content_publishing_limit', `${FB}/${ID}/content_publishing_limit`, {});
await get('ig host id', `https://graph.instagram.com/v23.0/${ID}`, { fields: 'id,username' });
