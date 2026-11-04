---
channel: li-nikita
at: 2026-11-17T09:15+01:00
type: text
media:
---
A degree of longitude isn't a fixed distance. We learned it in Rome.

Nesso turns coordinates into metres with a simple flat projection, and its scale was set at Turin's latitude, 45.07°. Rome is at 41.89°. One degree of longitude is 78,618 m at Turin and 82,865 m at Rome, so every east-west distance we computed in Rome came out 5.1% short: distance to water, the area around each hexagon, even which hexagons counted as inhabited.

Walk times survived. They are routed along the street graph, and every edge is measured on the sphere.

The fix wasn't a better constant. Each city now gets its own projection, and there is no default to fall back on, because a default is how it happened in the first place.

#geospatial #opendata #proptech
