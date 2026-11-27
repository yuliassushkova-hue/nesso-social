---
channel: li-nikita
at: 2026-11-19T09:15+01:00
type: text
media:
---
In Italian, "piano" means both the floor a flat is on and how many storeys a building has. One real listing we tested had both, a dozen words apart: "1 piano" (one storey) and "piano terra" (ground floor).

A parser that reads "1 piano" as first floor isn't almost right. It records the wrong fact about the flat, and the wrong fact looks exactly like a right one.

So Nesso reads a floor only when the ordinal is written: "2° piano", "secondo piano". A bare "1 piano" stays empty.

An empty field shows on screen and costs nothing. A wrong number travels everywhere the flat is shown.

#proptech #realestate #data
