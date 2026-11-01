# What we post, for whom, and how it looks

Read this before drafting a post. It is a summary of the launch campaign *Prima di firmare*; the
sources are in `nesso_mobile`, and where they disagree with this file, they win:

- `docs/marketing/campaign-plan-prima-di-firmare.md`: the plan (2 Nov 2026 to 31 Jan 2027)
- `docs/marketing/kit/`: links, week 1 posts, video scripts, the €12 Meta test
- `docs/press/PLAN.md` and `docs/press/social/drafts/`: positioning, and drafted posts with checked figures

## The idea

🇮🇹 *Il secondo parere sulla casa, prima di firmare.* · 🇬🇧 *The second opinion on a home, before you sign.*
· 🇩🇰 *Før du skriver under* (Danish waits on a native reader).

The enemy is the **information gap**, never agents as people: the listing is written by the seller,
the agent is paid by the deal, and the person signing has twenty minutes at a viewing and nothing in
their hands. Nesso is on their side, and only they pay.

## Who we talk to

Four groups (founder, 2026-10-21). **Never students**: no ESN, universities or student-season hooks.

| Group | Where | What hooks them | Show first |
|---|---|---|---|
| 1. First-home buyers, couples and families 28 to 45 | all Italian cities, Milano first; København, Aarhus | "What does this really cost, and what am I missing at a 20-minute viewing?" | costs calculator, viewing checklist, couples mode |
| 2. People relocating for work | Milano, Roma, Firenze, Torino; København, Aarhus | "I don't know this city or its rules, and can't afford one wrong flat." | the Live quiz, district rankings, the app in English |
| 3. Private investors | Milano, Torino, Genova; the Danish postcode map | "Which districts' published figures move, and what are the short-let rules?" | the Investment map, follow a district |
| 4. Sellers and landlords | all | "What makes a buyer pay more?" | Prepare (light now, full push in spring) |

In one picture: a couple or a professional moving to Milano or København, about to view flats, afraid
of signing something they will regret. They care most about **not being fooled and not overpaying**.

## Four messages

| # | Message | Proof (in the app today) |
|---|---|---|
| 1 | **Know the neighbourhood before the flat.** | OMI, Banca d'Italia, ISTAT, OpenStreetMap, Finans Danmark; 10 Italian and 5 Danish cities |
| 2 | **Your phone is the check at the viewing**, and it says what it cannot measure. | noise open and shut, daylight at the back wall, floor slope, sun over the building opposite, real floor |
| 3 | **Know the real cost, not the asking price.** | `/costs`, `nesso.fit/it/costi-acquisto-casa` |
| 4 | **Nobody is paid for your yes.** €1,99 or €6,99 a month; sellers and agents pay nothing and see nothing. | pricing page, terms |

## Instagram and Threads

- **Show, don't tell**: a phone measuring something, the number on screen, one line of text. Italian
  first; Denmark in English until a native reader has read the Danish.
- **The series is *Prima di firmare*.** Covers read **PRIMA DI FIRMARE · 01**, **· 02**, so the grid
  reads as a series.
- **Look**: cream ground, ink type, one orange accent (the app's own palette, Plus Jakarta Sans), the
  phone in frame. The app's houses and pins are already drawn and may be used. Real app screens only:
  `docs/marketing/mockups-it/` (framed, with headline) and `screens-it/`.
- **Video**: 9:16, 25 to 40 s, subtitles burned in, the hook in the first 1,5 s, platform-library music
  without lyrics. Film the phone and hands, never a stranger's home without the owner's yes, and film
  the real measurement (if the app refuses a reading, film a better window, never stage a number).
- **Links**: captions do not make links clickable on Instagram. The bio link is
  `nesso.fit/it/checklist-visita-casa?via=instagram`; captions say *link in bio*. Threads links carry
  `?via=threads`. Lowercase, exactly as written, or the sign-up is counted as `other`.
- **Calendar** (Italy): week 1 noise video, week 2 the real cost of a €300.000 flat, week 3 the quiz
  persona, week 4 city carousels on *Qualità della vita* (~1 Dec), then the sun, couples mode, and
  *what the app cannot measure*. The full table is in the campaign plan §7.

## Words

- **Never**, in any language: *sicuro / safe / sikker* about a place, *il migliore / the best place*,
  *in ascesa / up-and-coming*, *dove investire*, *redditizio / profitable*, *garantito*, *conviene*,
  price forecasts, user counts, *AI agents*, *this is advice*. Say *place N of M* or *top third*.
- **Every figure comes from a live public page** and names its source (`Fonte: OMI`, `Banca d'Italia`).
  Recheck an example on the live calculator before posting it.
- Say *è un calcolo sulle regole nazionali, non una consulenza* where a post adds up costs.
- No em dashes. Italian says *tu*. Do not promote Concierge.
- **Write like a person, not a chatbot.** Follow the `plain-human-writing` skill and run its scan on
  every caption and on-screen line before a post goes in a batch:
  `python3 ~/.claude/skills/plain-human-writing/scripts/scan.py --lang it post.md`. It catches
  *gioca un ruolo fondamentale*, *non solo… ma anche*, *nel cuore di*, *è importante notare*, emoji
  bullets and Markdown that will not render.
- A paid or gifted post carries *Pubblicità* / *ADV* (Italy) or *Reklame* (Denmark).

## The weekly cycle

1. **Sunday: the batch.** A content session writes `weeks/<monday>.py` (every caption, card and
   slide, with where each figure comes from), runs `tools/render.py` on it, and opens one pull
   request with the whole week in `posts/`.
2. **The PR checks itself.** `check` validates every post; `rehearse` has Instagram fetch and process
   every image and video without publishing, so a file Instagram would refuse is found before the
   week starts.
3. **The founder approves by merging.** Anything to drop is deleted from the branch first.
4. **Publish runs every ten minutes.** Rome times: Reels 08:00, 13:00, 20:00; carousels 18:00 (Mon, Wed, Fri,
   Sun); Stories 09:30, 15:30, 21:30.
5. **Monday: what worked.** Reach, saves, shares and profile visits per post (Instagram Insights),
   and sign-ups with `via=instagram` in `/admin`. Series that do not travel are replaced the next
   Sunday; the volume stays.

**Formats.** *Prima di firmare* (one viewing check: hook, the app's steps, what it does not
establish, link in bio) · *Quanto costa* (one cost rule with the figure) · *Mito o no* (a selling
myth and what the research found) · app screen recordings · carousels of 6 to 9 slides with a cover
that makes the claim and a phone on it.

**What the API cannot do**, so a person does it in the app when it matters: music from Instagram's
library, poll and link stickers on Stories, replying to comments (until the comments permission is
added), and anything on TikTok (a TikTok account and its Content Posting API approval come first).
