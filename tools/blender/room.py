"""An isometric cut-away flat, the way Airbnb's Buck films show a room: a slab with two walls,
small rounded furniture, one big soft light. A phone carrying the real app screen floats in, the
window opens, orange sound rings spread from it, the window shuts and the rings shrink.

    blender -b -P tools/blender/room.py -- <frames dir> [seconds] [phone image]
    STILLS=30,150 blender -b -P tools/blender/room.py -- <dir>     # only those frames

Frames are 1080x1920 JPEG at 30 fps; tools/render.py lays the words over the top third.
"""
import math
import os
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else "/tmp/room/"
SECONDS = float(argv[1]) if len(argv) > 1 else 12
PHONE = argv[2] if len(argv) > 2 else os.path.join(os.path.dirname(__file__), "phone-rumore.png")
FPS = 30


def srgb(hex_):
    h = hex_.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


VIOLET, NIGHT, PLUM, ORANGE, ORANGE_LIGHT = "#5A3EC0", "#34216F", "#7D3AA8", "#F97316", "#FFAF5E"
CREAM, PAPER, WOOD, INK, SKY = "#FFF4EC", "#FFFFFF", "#E9C9A6", "#1B1D22", "#BFD7F2"

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.resolution_x, scene.render.resolution_y = 1080, 1920
scene.render.fps = FPS
scene.frame_start, scene.frame_end = 1, round(SECONDS * FPS)
for engine in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
    try:
        scene.render.engine = engine
        break
    except TypeError:
        continue
try:
    scene.eevee.taa_render_samples = 24
except AttributeError:
    pass
scene.view_settings.view_transform = "Standard"
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 95  # a cached scene is about 100 MB as JPEG, 700 MB as PNG
scene.render.filepath = OUT.rstrip("/") + "/"


def material(name, hex_, rough=0.7, emit=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = srgb(hex_)
    bsdf.inputs["Roughness"].default_value = rough
    if emit:
        bsdf.inputs["Emission Color"].default_value = srgb(hex_)
        bsdf.inputs["Emission Strength"].default_value = emit
    return m


MATS = {}


def mat(hex_, rough=0.7):
    if (hex_, rough) not in MATS:
        MATS[(hex_, rough)] = material(f"m{len(MATS)}", hex_, rough)
    return MATS[(hex_, rough)]


def box(size, loc, color, bevel=0.04, parent=None, rough=0.7):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    if bevel:
        mod = o.modifiers.new("bevel", "BEVEL")
        mod.width, mod.segments = bevel, 4
        mod.limit_method = "ANGLE"
    for p in o.data.polygons:
        p.use_smooth = True
    o.data.materials.append(mat(color, rough))
    if parent:
        o.parent = parent
    return o


def cyl(r, depth, loc, color, parent=None, verts=48, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth, location=loc, vertices=verts, rotation=rot)
    o = bpy.context.object
    for p in o.data.polygons:
        p.use_smooth = True
    o.data.materials.append(mat(color))
    if parent:
        o.parent = parent
    return o


def ball(r, loc, color, parent=None):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=40, ring_count=20)
    o = bpy.context.object
    for p in o.data.polygons:
        p.use_smooth = True
    o.data.materials.append(mat(color))
    if parent:
        o.parent = parent
    return o


def key(obj, frame, **values):
    for attr, value in values.items():
        setattr(obj, attr, value)
        obj.keyframe_insert(data_path=attr, frame=frame)


def empty(name, loc=(0, 0, 0)):
    e = bpy.data.objects.new(name, None)
    scene.collection.objects.link(e)
    e.location = loc
    return e


def pop(obj, at, size=1.0):
    """Arrive by scaling up past full size and settling, the Buck way of placing a prop."""
    key(obj, 1, scale=(0.001,) * 3)
    key(obj, at, scale=(0.001,) * 3)
    key(obj, at + 7, scale=(size * 1.1,) * 3)
    key(obj, at + 12, scale=(size,) * 3)


world = bpy.data.worlds.new("world")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = srgb(VIOLET)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0

# The ground the room floats over: same violet as the world, so there is no horizon.
bpy.ops.mesh.primitive_plane_add(size=400, location=(0, 0, -1.2))
bpy.context.object.data.materials.append(material("ground", VIOLET, 0.9))

# ---------------------------------------------------------------- the room
room = empty("room")
S, WH, T = 4.0, 2.7, 0.18  # floor side, wall height, wall thickness
box((S, S, 0.3), (0, 0, -0.15), WOOD, 0.06, room)               # floor slab
box((S, T, WH), (0, S / 2 - T / 2, WH / 2), CREAM, 0.03, room)  # back wall
box((T, S, WH), (-S / 2 + T / 2, 0, WH / 2), CREAM, 0.03, room)  # left wall
box((2.4, 1.8, 0.03), (0.2, -0.1, 0.02), PLUM, 0.01, room)       # rug

# The window, in the back wall: frame, sky behind, and a sash that swings open.
win = empty("window", (0.65, S / 2 - T - 0.09, 1.55))
win.parent = room
box((1.25, 0.04, 1.2), (0, 0.04, 0), SKY, 0, win, rough=0.3)
for dx, dz, sx, sz in [(0, 0.62, 1.4, 0.1), (0, -0.62, 1.4, 0.1), (-0.66, 0, 0.1, 1.34), (0.66, 0, 0.1, 1.34)]:
    box((sx, 0.14, sz), (dx, 0, dz), PAPER, 0.02, win)
hinge = empty("hinge", (-0.6, -0.05, 0))
hinge.parent = win
for dx, dz, sx, sz in [(0.6, 0.55, 1.2, 0.07), (0.6, -0.55, 1.2, 0.07), (0.03, 0, 0.07, 1.17), (1.17, 0, 0.07, 1.17), (0.6, 0, 0.05, 1.1)]:
    box((sx, 0.06, sz), (dx, 0, dz), ORANGE, 0.015, hinge)

# Furniture, all rounded and matte.
sofa = empty("sofa", (-0.9, 0.95, 0))
sofa.parent = room
box((1.9, 0.75, 0.42), (0, 0, 0.21), ORANGE, 0.12, sofa)
box((1.9, 0.22, 0.75), (0, 0.3, 0.55), ORANGE, 0.1, sofa)
for x in (-0.95, 0.95):
    box((0.2, 0.75, 0.6), (x, 0, 0.3), ORANGE, 0.08, sofa)
box((0.55, 0.15, 0.4), (-0.35, 0.1, 0.62), ORANGE_LIGHT, 0.08, sofa)

lamp = empty("lamp", (1.45, 1.35, 0))
lamp.parent = room
cyl(0.2, 0.05, (0, 0, 0.03), INK, lamp)
cyl(0.03, 1.5, (0, 0, 0.78), INK, lamp)
bpy.ops.mesh.primitive_cone_add(radius1=0.32, radius2=0.18, depth=0.36, location=(0, 0, 1.62), vertices=48)
shade = bpy.context.object
shade.data.materials.append(material("shade", ORANGE_LIGHT, 0.6, emit=0.6))
shade.parent = lamp

plant = empty("plant", (-1.55, -1.3, 0))
plant.parent = room
cyl(0.24, 0.42, (0, 0, 0.21), PAPER, plant)
for x, y, z, r in [(0, 0, 0.62, 0.3), (0.16, -0.1, 0.85, 0.22), (-0.14, 0.08, 0.92, 0.2)]:
    ball(r, (x, y, z), "#2F8F5B", plant)

table = empty("table", (0.35, -0.35, 0))
table.parent = room
cyl(0.5, 0.06, (0, 0, 0.42), PAPER, table)
cyl(0.05, 0.4, (0, 0, 0.2), INK, table)
cyl(0.09, 0.14, (0.18, 0.1, 0.52), VIOLET, table)  # a mug

frame_ = empty("picture", (-S / 2 + T + 0.02, -0.4, 1.7))
frame_.parent = room
box((0.04, 0.9, 0.65), (0, 0, 0), INK, 0.02, frame_)
box((0.03, 0.78, 0.53), (0.02, 0, 0), ORANGE_LIGHT, 0.0, frame_)

# The room builds itself, piece by piece.
for i, obj in enumerate([sofa, table, lamp, plant, frame_, win]):
    pop(obj, 4 + i * 4)
key(room, 1, rotation_euler=(0, 0, math.radians(-8)))
key(room, scene.frame_end, rotation_euler=(0, 0, math.radians(6)))

# ---------------------------------------------------------------- the phone, with the real app screen
img = bpy.data.images.load(PHONE)
aspect = img.size[1] / img.size[0]
ph = empty("phone", (1.1, -1.6, 1.9))
pw, phh = 0.85, 0.85 * aspect
body = box((pw * 1.02, 0.08, phh * 1.01), (0, 0.045, 0), INK, 0.05, ph, rough=0.3)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, -0.002, 0), rotation=(math.pi / 2, 0, 0))
screen = bpy.context.object
screen.scale = (pw, phh, 1)
sm = bpy.data.materials.new("screen")
sm.use_nodes = True
nodes, links = sm.node_tree.nodes, sm.node_tree.links
nodes.clear()
tex = nodes.new("ShaderNodeTexImage")
tex.image = img
emit = nodes.new("ShaderNodeEmission")
emit.inputs["Strength"].default_value = 1.0
transp = nodes.new("ShaderNodeBsdfTransparent")
mix = nodes.new("ShaderNodeMixShader")
outn = nodes.new("ShaderNodeOutputMaterial")
links.new(tex.outputs["Color"], emit.inputs["Color"])
links.new(tex.outputs["Alpha"], mix.inputs["Fac"])
links.new(transp.outputs["BSDF"], mix.inputs[1])
links.new(emit.outputs["Emission"], mix.inputs[2])
links.new(mix.outputs["Shader"], outn.inputs["Surface"])
try:
    sm.surface_render_method = "DITHERED"
except AttributeError:
    pass
screen.data.materials.append(sm)
screen.parent = ph
# Flies in from the lower right, turns to face the viewer, then floats.
key(ph, 1, location=(7.0, -8.0, -3.0), rotation_euler=(0, 0, math.radians(-60)))
key(ph, 34, location=(7.0, -8.0, -3.0), rotation_euler=(0, 0, math.radians(-60)))
key(ph, 52, location=(2.35, -2.55, 1.7), rotation_euler=(math.radians(-8), 0, math.radians(30)))
end = scene.frame_end
for f in range(70, end, 30):
    key(ph, f, location=(2.35, -2.55, 1.7 + (0.08 if (f // 30) % 2 else -0.08)), rotation_euler=(math.radians(-8), 0, math.radians(30)))

# ---------------------------------------------------------------- the window opens, sound comes in
open_at, shut_at = 95, round(SECONDS * FPS * 0.62)
key(hinge, 1, rotation_euler=(0, 0, 0))
key(hinge, open_at, rotation_euler=(0, 0, 0))
key(hinge, open_at + 10, rotation_euler=(0, 0, math.radians(-75)))
key(hinge, shut_at, rotation_euler=(0, 0, math.radians(-75)))
key(hinge, shut_at + 10, rotation_euler=(0, 0, 0))

ring_mat = material("ring", ORANGE, 0.4, emit=1.5)
waves = empty("waves", (0.65, S / 2 - T - 0.2, 1.55))
waves.parent = room
for i in range(5):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.5, minor_radius=0.035, location=(0, 0, 0), rotation=(math.pi / 2, 0, 0))
    ring = bpy.context.object
    ring.data.materials.append(ring_mat)
    ring.parent = waves
    period = 36
    # loud while open: big rings spreading out; quiet once shut: small ones
    f = open_at + 10 + i * (period // 5)
    while f < end:
        loud = f < shut_at
        grow = 2.4 if loud else 1.1
        key(ring, f, scale=(0.4, 0.4, 0.4), location=(0, 0, 0))
        key(ring, f + period - 2, scale=(grow, grow, grow), location=(0, -0.9 if loud else -0.3, 0))
        key(ring, f + period - 1, scale=(0.001,) * 3, location=(0, 0, 0))
        f += period
    key(ring, 1, scale=(0.001,) * 3)
    key(ring, open_at + 9 + i * (period // 5), scale=(0.001,) * 3)

# ---------------------------------------------------------------- light and the isometric camera
bpy.ops.object.light_add(type="AREA", location=(-5, -6, 9))
key_light = bpy.context.object
key_light.data.size, key_light.data.energy = 9, 2600
key_light.rotation_euler = (math.radians(45), 0, math.radians(-40))
bpy.ops.object.light_add(type="AREA", location=(6, -2, 4))
fill = bpy.context.object
fill.data.size, fill.data.energy = 6, 700
fill.data.color = srgb(ORANGE_LIGHT)[:3]
fill.rotation_euler = (math.radians(70), 0, math.radians(60))

bpy.ops.object.camera_add()
cam = bpy.context.object
scene.camera = cam
cam.data.type = "ORTHO"
cam.data.ortho_scale = 11.0
cam.rotation_euler = (math.radians(58), 0, math.radians(38))
# Pushed up so the room sits in the lower two thirds and the words have the top.
cam.location = (8.4, -10.8, 11.9)
key(cam, 1, location=cam.location.copy())
key(cam, end, location=(8.0, -10.4, 11.5))

stills = os.environ.get("STILLS")
if stills:
    for f in [int(x) for x in stills.split(",")]:
        scene.frame_set(f)
        scene.render.filepath = OUT.rstrip("/") + f"/still_{f:04d}.jpg"
        bpy.ops.render.render(write_still=True)
else:
    bpy.ops.render.render(animation=True)
