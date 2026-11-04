---
channel: li-nikita
at: 2026-11-24T09:15+01:00
type: text
media:
---
In 1987 Robert Solow wrote that you can see the computer age everywhere but in the productivity statistics. Coding with AI has its own version: more code, and more of it that nothing calls.

One day in September we used our app on a real phone and found six defects that day. Every one sat behind green tests. The function deciding whether to install the offline service worker was correct, tested nine ways, and called by nothing, so no phone had ever installed it. The retry queue for saves computed the right wait and nothing waited, so one failed save jammed it for good.

What we wrote down: a test that a decision is correct is not a test that anything acts on it. Now a new module and its caller land in the same commit.

#softwareengineering #ai #testing
