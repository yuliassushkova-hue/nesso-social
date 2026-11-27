---
channel: li-nikita
at: 2026-11-12T09:15+01:00
type: text
media:
---
Context engineering is the skill people keep naming for building with AI agents. This is what it looks like in our codebase.

Nesso has 7,259 lines of written decisions in 93 files, and a 195-line index the agents read before they touch anything. They aren't style rules. Each one is a decision with its reason and the bug that taught it: why a missing figure is shown as "not checked" and never as zero, why each city needs its own map projection, why the word "safe" fails the build.

That last one is literal. A lint reads every string a user can see, in English, Italian and German, and the build fails on "safe", "up-and-coming", "guaranteed" or "profitable". A model will happily describe "a safe neighbourhood". We can't publish that.

Behind it sit 491 test files. The agents are fast; the written decisions keep them pointed the same way.

#ai #softwareengineering #proptech
