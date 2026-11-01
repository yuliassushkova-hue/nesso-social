# nesso-social

Nesso's posts for four channels: Instagram in Italian and Danish, and Threads in Italian and Danish.
Posts are written in a content session (read `STRATEGY.md` first), approved by merging, and published on schedule by GitHub
Actions. `SETUP.md` is how the accounts and secrets are connected (in Russian).

## How a post goes out

1. **A content session drafts posts on a branch** and opens a pull request. One folder per post.
2. **`check` runs on the PR** and fails on anything the platform would refuse: a PNG on Instagram,
   eleven carousel slides, a caption over the limit, a time with no offset.
3. **You read the PR and merge it. Merging is the approval.** Nothing on a branch is ever published.
   To hold a post back, don't merge it. To cancel one already on `main`, delete its folder before its
   time.
4. **`publish` runs every hour at :07** and publishes each post whose time has passed, so a post set
   for 18:00 goes out between 18:07 and about 18:30 (GitHub's schedule can run late).
5. **`published.json` records each post** with its link, committed back to `main`. A post in that
   file is never published again. A post more than 36 hours late is skipped and reported instead of
   going out days after its moment.

There is no edit after publishing: fix a published post in the app itself.

## A post

```
posts/2026-11-04-ig-it-costi/
  post.md
  01.jpg
  02.jpg
```

```markdown
---
channel: ig-it                   # ig-it | ig-dk | threads-it | threads-dk
at: 2026-11-04T18:00+01:00       # always with the offset: +01:00 Rome and Copenhagen in winter, +02:00 in summer
type: carousel                   # Instagram: image | carousel | reel | story   Threads: text | image | video | carousel
media: 01.jpg, 02.jpg            # in order; empty for a Threads text post
---
The caption, exactly as it will appear. Line breaks are kept.

#casa #affitto
```

| | Instagram | Threads |
|---|---|---|
| images | JPEG only | JPEG or PNG |
| video | MP4 or MOV | MP4 or MOV |
| caption | 2200 characters, 30 hashtags | 500 characters |
| carousel | 2 to 10 | 2 to 20 |

Convert a PNG for Instagram with `sips -s format jpeg -s formatOptions 90 in.png --out 01.jpg`. Feed
images are best at 1080×1350 (4:5); stories and reels at 1080×1920.

Name folders `YYYY-MM-DD-channel-subject`, so the folder list reads as the calendar.

## Rules for the words

The copy is Nesso speaking in public, so the product's own rules apply (see `CLAUDE.md` §3 in
`nesso_mobile`):

- **Copy follows the app.** Prices, plan names and features are what the app has today. A feature
  that is *Coming soon* in the app is not presented as available.
- **None of the banned claims, in any language**: nothing is *safe*, *sicuro* (about a place),
  *guaranteed*, *garantito*, *profitable*, *will appreciate*, *up-and-coming*, *dangerous*. Nesso
  records what was checked; it does not inspect, value or advise.
- **No em dashes.**
- **Danish needs a native reader before it is merged.** The app's own Danish is drafted and waits on
  a native review; posts in Danish wait on the same.
- Figures quoted from a source name it (`Fonte: Banca d'Italia`, `OMI`, `ISTAT`).

## Commands

```bash
node bin/social.mjs check              # validate the queue (also runs on every PR)
node bin/social.mjs list               # the schedule and the state of each post
node bin/social.mjs publish --dry-run  # what would go out now
```

`publish`, `whoami`, `refresh-tokens` and `exchange-threads` need the secrets and run in Actions.
