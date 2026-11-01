"""A flat cut open like a doll's house, after Airbnb's films by Buck: a pale studio ground, a lived-in
room with real furniture and warm lamps, and two soft little people. One sits on the sofa with the
app open on a phone; the other opens the window, and the sound of the street comes in.

    blender -b -P tools/blender/home.py -- <frames dir> [seconds]
    STILLS=40,200 blender -b -P tools/blender/home.py -- <dir>

Furniture and textures: Poly Haven (CC0), in ~/Documents/GitHub/nesso-assets/polyhaven.
The people are built here from soft shapes. JPEG frames, 1080x1920, 30 fps.
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else "/tmp/home/"
SECONDS = float(argv[1]) if len(argv) > 1 else 12
ASSETS = os.path.expanduser("~/Documents/GitHub/nesso-assets/polyhaven")
PHONE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phone-rumore.png")
FPS = 30


def srgb(hex_):
    h = hex_.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


GROUND, WALL, TRIM = "#EAE6E1", "#F6F1EA", "#FFFFFF"
ORANGE, ORANGE_LIGHT, VIOLET, PLUM, NIGHT = "#F97316", "#FFAF5E", "#5A3EC0", "#7D3AA8", "#34216F"
SKIN_A, SKIN_B, HAIR_A, HAIR_B = "#E8B48F", "#9C6644", "#3B2A22", "#1E1A1A"
DENIM, CREAM, INK, SKY = "#3F5B8C", "#F4E9DA", "#2A2A2E", "#CFE3F5"

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
ev = scene.eevee
for attr, value in (("taa_render_samples", 48), ("use_raytracing", True), ("use_shadows", True)):
    try:
        setattr(ev, attr, value)
    except (AttributeError, TypeError):
        pass
try:
    ev.ray_tracing_options.resolution_scale = "2"
except Exception:
    pass
scene.view_settings.view_transform = "AgX"
try:
    scene.view_settings.look = "AgX - Medium High Contrast"
except TypeError:
    pass
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 95
scene.render.filepath = OUT.rstrip("/") + "/"

MATS = {}


def mat(hex_, rough=0.7, sheen=0.0, emit=0.0):
    k = (hex_, rough, sheen, emit)
    if k in MATS:
        return MATS[k]
    m = bpy.data.materials.new(f"m{len(MATS)}")
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = srgb(hex_)
    b.inputs["Roughness"].default_value = rough
    if sheen:
        b.inputs["Sheen Weight"].default_value = sheen
    if emit:
        b.inputs["Emission Color"].default_value = srgb(hex_)
        b.inputs["Emission Strength"].default_value = emit
    MATS[k] = m
    return m


def smooth(o, levels=2):
    for p in o.data.polygons:
        p.use_smooth = True
    if levels:
        o.modifiers.new("sub", "SUBSURF").levels = levels


def box(size, loc, color, bevel=0.02, parent=None, rough=0.7):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    if bevel:
        b = o.modifiers.new("bevel", "BEVEL")
        b.width, b.segments = bevel, 3
    for p in o.data.polygons:
        p.use_smooth = True
    o.data.materials.append(mat(color, rough))
    if parent:
        o.parent = parent
    return o


def blob(scale, loc, color, parent=None, rough=0.6, sheen=0.0):
    """A soft ellipsoid: the people are made of these."""
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=loc, segments=32, ring_count=16)
    o = bpy.context.object
    o.scale = scale
    smooth(o, 1)
    o.data.materials.append(mat(color, rough, sheen))
    if parent:
        o.parent = parent
    return o


def empty(name, loc=(0, 0, 0), parent=None):
    e = bpy.data.objects.new(name, None)
    scene.collection.objects.link(e)
    e.location = loc
    if parent:
        e.parent = parent
    return e


def key(obj, frame, **values):
    for attr, value in values.items():
        setattr(obj, attr, value)
        obj.keyframe_insert(data_path=attr, frame=frame)


def asset(name, loc, rot_z=0.0, scale=1.0, parent=None):
    """Import a Poly Haven model, grouped under one empty standing on its own floor point."""
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=f"{ASSETS}/{name}/{name}.gltf")
    new = [o for o in bpy.data.objects if o not in before]
    root = empty(name, loc, parent)
    for o in new:
        if o.parent is None:
            o.parent = root
    root.rotation_euler = (0, 0, rot_z)
    root.scale = (scale,) * 3
    return root


# ---------------------------------------------------------------- the studio: pale, seamless, soft
world = bpy.data.worlds.new("world")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = srgb(GROUND)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.55
bpy.ops.mesh.primitive_plane_add(size=400, location=(0, 0, -0.32))
bpy.context.object.data.materials.append(mat(GROUND, 0.9))

# ---------------------------------------------------------------- the room
room = empty("room")
S, WH, T = 4.4, 2.75, 0.16
floor = box((S, S, 0.3), (0, 0, -0.15), "#C99A6B", 0.02, room)
fm = bpy.data.materials.new("floor")
fm.use_nodes = True
nodes, links = fm.node_tree.nodes, fm.node_tree.links
bsdf = nodes["Principled BSDF"]
coord = nodes.new("ShaderNodeTexCoord")
mapping = nodes.new("ShaderNodeMapping")
mapping.inputs["Scale"].default_value = (1.3, 1.3, 1.3)
links.new(coord.outputs["Object"], mapping.inputs["Vector"])
for kind, inp, colour in (("Diffuse", "Base Color", True), ("Rough", "Roughness", False)):
    t = nodes.new("ShaderNodeTexImage")
    t.image = bpy.data.images.load(f"{ASSETS}/wooden_floor_02/{kind}.jpg")
    if not colour:
        t.image.colorspace_settings.name = "Non-Color"
    links.new(mapping.outputs["Vector"], t.inputs["Vector"])
    links.new(t.outputs["Color"], bsdf.inputs[inp])
floor.data.materials[0] = fm
box((S, T, WH), (0, S / 2 - T / 2, WH / 2), WALL, 0.01, room, rough=0.9)
box((T, S, WH), (-S / 2 + T / 2, 0, WH / 2), WALL, 0.01, room, rough=0.9)
box((S, 0.03, 0.1), (0, S / 2 - T - 0.015, 0.05), TRIM, 0.005, room)   # skirting
box((0.03, S, 0.1), (-S / 2 + T + 0.015, 0, 0.05), TRIM, 0.005, room)

# Rug, in the brand violet, with a fine weave.
rug = box((2.3, 1.6, 0.02), (0.15, -0.15, 0.012), VIOLET, 0.01, room, rough=0.95)
rug.data.materials[0] = mat(VIOLET, 0.95, sheen=0.6)

# Window in the back wall: sky, frame, a sash that swings open, curtains that move in the air.
win = empty("window", (0.95, S / 2 - T - 0.03, 1.5), room)
box((1.2, 0.02, 1.25), (0, 0.04, 0), SKY, 0, win, rough=0.2).data.materials[0] = mat(SKY, 0.2, emit=0.8)
for dx, dz, sx, sz in [(0, 0.66, 1.36, 0.08), (0, -0.66, 1.36, 0.08), (-0.64, 0, 0.08, 1.4), (0.64, 0, 0.08, 1.4)]:
    box((sx, 0.1, sz), (dx, 0, dz), TRIM, 0.01, win)
hinge = empty("hinge", (-0.58, -0.04, 0), win)
for dx, dz, sx, sz in [(0.58, 0.57, 1.16, 0.05), (0.58, -0.57, 1.16, 0.05), (0.02, 0, 0.05, 1.18), (1.14, 0, 0.05, 1.18)]:
    box((sx, 0.05, sz), (dx, 0, dz), TRIM, 0.008, hinge)
for side in (-1, 1):
    bpy.ops.mesh.primitive_plane_add(size=1, location=(side * 0.86, -0.08, -0.02), rotation=(math.pi / 2, 0, 0))
    cur = bpy.context.object
    cur.scale = (0.38, 1.6, 1)
    cur.parent = win
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.subdivide(number_cuts=24)
    bpy.ops.object.mode_set(mode="OBJECT")
    w = cur.modifiers.new("folds", "WAVE")
    w.use_x, w.use_y, w.height, w.width, w.narrowness, w.speed = True, False, 0.035, 0.18, 1.0, 0.01
    w.use_normal = True
    cur.data.materials.append(mat(CREAM, 0.9, sheen=0.4))
    smooth(cur, 0)

# Real furniture (Poly Haven, CC0).
asset("Sofa_01", (-0.75, 1.55, 0), 0.0, 1.25, room)
pillows = asset("throw_pillows_01", (-0.75, 1.62, 0.36), 0.0, 0.75, room)
asset("modern_arm_chair_01", (-1.62, -0.45, 0), math.radians(90), 1.0, room)  # back to the left wall, facing the room
asset("coffee_table_round_01", (0.1, -0.05, 0), 0, 0.85, room)
asset("tea_set_01", (0.1, -0.05, 0.42), 0.4, 0.55, room)
asset("potted_plant_01", (0.25, 1.75, 0), 0, 1.0, room)
asset("potted_plant_02", (1.75, -1.6, 0), 0.6, 1.0, room)
asset("side_table_01", (1.75, 1.6, 0), 0, 1.0, room)

# A floor lamp, warm and on.
lamp = empty("lamp", (-1.75, 0.75, 0), room)  # beside the sofa, clear of the window
bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=0.04, location=(0, 0, 0.02), vertices=40)
bpy.context.object.data.materials.append(mat(INK, 0.4))
bpy.context.object.parent = lamp
bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=1.55, location=(0, 0, 0.8), vertices=16)
bpy.context.object.data.materials.append(mat(INK, 0.4))
bpy.context.object.parent = lamp
bpy.ops.mesh.primitive_cone_add(radius1=0.3, radius2=0.2, depth=0.34, location=(0, 0, 1.65), vertices=48)
bpy.context.object.data.materials.append(mat("#FFE2B8", 0.8, emit=2.5))
bpy.context.object.parent = lamp
bpy.ops.object.light_add(type="POINT", location=(-1.75, 0.75, 1.55))
bulb = bpy.context.object
bulb.data.energy, bulb.data.color, bulb.data.shadow_soft_size = 120, (1.0, 0.72, 0.45), 0.3
bulb.parent = room

# A picture on the left wall: the Nesso orange, framed.
box((0.04, 0.9, 0.62), (-S / 2 + T + 0.02, -0.2, 1.65), INK, 0.01, room)
box((0.03, 0.8, 0.52), (-S / 2 + T + 0.04, -0.2, 1.65), ORANGE, 0.0, room)


# ---------------------------------------------------------------- the people
def person(name, loc, rot_z, skin, hair, top, bottom, hair_style="bob"):
    """A soft little person: about 1.55 tall, simple face, clothes in flat matte colour.
    Returns the joints so a pose and an animation can be put on them."""
    root = empty(name, loc)
    root.rotation_euler = (0, 0, rot_z)
    j = {"root": root}
    hips = empty(name + "_hips", (0, 0, 0.82), root)
    j["hips"] = hips
    blob((0.17, 0.12, 0.13), (0, 0, 0.0), bottom, hips, sheen=0.3)
    for side in (-1, 1):
        hip = empty(f"{name}_hip{side}", (side * 0.085, 0, -0.04), hips)
        blob((0.075, 0.075, 0.23), (0, 0, -0.2), bottom, hip, sheen=0.3)
        knee = empty(f"{name}_knee{side}", (0, 0, -0.41), hip)
        blob((0.062, 0.062, 0.21), (0, 0, -0.19), bottom, knee, sheen=0.3)
        blob((0.06, 0.11, 0.045), (0, -0.04, -0.4), INK, knee, rough=0.4)  # shoe
        j[f"hip{side}"], j[f"knee{side}"] = hip, knee
    chest = empty(name + "_chest", (0, 0, 0.05), hips)
    j["chest"] = chest
    blob((0.15, 0.105, 0.27), (0, 0, 0.25), top, chest, sheen=0.4)
    blob((0.045, 0.045, 0.06), (0, 0, 0.5), skin, chest)  # neck
    head = empty(name + "_head", (0, 0, 0.54), chest)
    j["head"] = head
    blob((0.12, 0.115, 0.135), (0, 0, 0.12), skin, head, rough=0.5)
    for side in (-1, 1):  # eyes and cheeks: the cute is in these
        blob((0.014, 0.008, 0.018), (side * 0.045, -0.108, 0.13), INK, head, rough=0.2)
        blob((0.022, 0.006, 0.014), (side * 0.065, -0.1, 0.085), "#F2A0A0", head, rough=0.6)
    if hair_style == "bob":
        blob((0.135, 0.13, 0.12), (0, 0.02, 0.17), hair, head, rough=0.45)
        blob((0.14, 0.11, 0.1), (0, 0.03, 0.08), hair, head, rough=0.45)
    else:  # a bun
        blob((0.128, 0.125, 0.1), (0, 0.015, 0.19), hair, head, rough=0.45)
        blob((0.07, 0.07, 0.07), (0, 0.06, 0.3), hair, head, rough=0.45)
    for side in (-1, 1):
        sh = empty(f"{name}_shoulder{side}", (side * 0.15, 0, 0.44), chest)
        blob((0.046, 0.046, 0.15), (0, 0, -0.13), top, sh, sheen=0.4)
        el = empty(f"{name}_elbow{side}", (0, 0, -0.27), sh)
        blob((0.038, 0.038, 0.13), (0, 0, -0.11), skin, el)
        blob((0.04, 0.035, 0.045), (0, 0, -0.25), skin, el)  # hand
        j[f"shoulder{side}"], j[f"elbow{side}"] = sh, el
    return j


def rot(o, frame, x=0, y=0, z=0):
    key(o, frame, rotation_euler=(math.radians(x), math.radians(y), math.radians(z)))


end = scene.frame_end

# Giulia, on the sofa, phone in both hands.
g = person("giulia", (-0.55, 1.15, 0.0), 0.0, SKIN_A, HAIR_A, ORANGE, DENIM, "bob")
g["root"].parent = room
g["hips"].location = (0, 0, 0.47)
for side in (-1, 1):
    # thighs forward, shins down; upper arms forward, forearms up to the phone
    rot(g[f"hip{side}"], 1, x=-88)
    rot(g[f"knee{side}"], 1, x=88)
    rot(g[f"shoulder{side}"], 1, x=-30, y=side * 8)
    rot(g[f"elbow{side}"], 1, x=-75, y=side * 12)
phone = empty("phone", (0, -0.36, 0.36), g["chest"])
img = bpy.data.images.load(PHONE)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0), rotation=(math.radians(70), 0, 0))
scr = bpy.context.object
scr.scale = (0.11, 0.11 * img.size[1] / img.size[0], 1)
sm = bpy.data.materials.new("screen")
sm.use_nodes = True
n, lk = sm.node_tree.nodes, sm.node_tree.links
n.clear()
tx = n.new("ShaderNodeTexImage")
tx.image = img
em = n.new("ShaderNodeEmission")
em.inputs["Strength"].default_value = 1.6
tr = n.new("ShaderNodeBsdfTransparent")
mx = n.new("ShaderNodeMixShader")
o_ = n.new("ShaderNodeOutputMaterial")
lk.new(tx.outputs["Color"], em.inputs["Color"])
lk.new(tx.outputs["Alpha"], mx.inputs["Fac"])
lk.new(tr.outputs["BSDF"], mx.inputs[1])
lk.new(em.outputs["Emission"], mx.inputs[2])
lk.new(mx.outputs["Shader"], o_.inputs["Surface"])
scr.data.materials.append(sm)
scr.parent = phone
# She looks at the phone, up at the window when it opens, and back.
open_at, shut_at = 110, round(end * 0.64)
rot(g["head"], 1, x=-18)
rot(g["head"], open_at, x=-18)
rot(g["head"], open_at + 12, x=4, z=-35)
rot(g["head"], shut_at + 10, x=4, z=-35)
rot(g["head"], shut_at + 24, x=-18)
for f in range(1, end, 45):  # breathing
    key(g["chest"], f, scale=(1, 1, 1))
    key(g["chest"], f + 22, scale=(1.015, 1.015, 1.02))

# Marco, at the window: walks to it, opens it, shuts it.
m = person("marco", (1.6, 0.2, 0.0), math.radians(160), SKIN_B, HAIR_B, PLUM, CREAM, "bun")
m["root"].parent = room
start, at_window = (1.6, 0.2, 0.0), (1.05, 1.45, 0.0)
key(m["root"], 1, location=start)
key(m["root"], 30, location=start)
key(m["root"], 85, location=at_window, rotation_euler=(0, 0, math.radians(180)))
for f in range(30, 86, 7):  # a little walk cycle
    s = 1 if (f // 7) % 2 else -1
    rot(m["hip-1"], f, x=s * 22)
    rot(m["hip1"], f, x=-s * 22)
    rot(m["shoulder-1"], f, x=-s * 18)
    rot(m["shoulder1"], f, x=s * 18)
for side in (-1, 1):
    rot(m[f"hip{side}"], 90, x=0)
    rot(m[f"shoulder{side}"], 90, x=0)
# reaches up to the handle and pulls
rot(m["shoulder1"], open_at - 14, x=0)
rot(m["shoulder1"], open_at - 4, x=-150, y=10)
rot(m["elbow1"], open_at - 4, x=-20)
rot(m["shoulder1"], open_at + 14, x=-60)
rot(m["shoulder1"], shut_at - 10, x=-60)
rot(m["shoulder1"], shut_at, x=-150, y=10)
rot(m["shoulder1"], shut_at + 14, x=0)
rot(m["elbow1"], shut_at + 14, x=0)
key(hinge, 1, rotation_euler=(0, 0, 0))
key(hinge, open_at, rotation_euler=(0, 0, 0))
key(hinge, open_at + 12, rotation_euler=(0, 0, math.radians(-80)))
key(hinge, shut_at, rotation_euler=(0, 0, math.radians(-80)))
key(hinge, shut_at + 12, rotation_euler=(0, 0, 0))

# The street, as faint orange rings coming in at the window: wide while it is open, small once shut.
ring_mat = bpy.data.materials.new("ring")
ring_mat.use_nodes = True
rn = ring_mat.node_tree.nodes
rn["Principled BSDF"].inputs["Base Color"].default_value = srgb(ORANGE)
rn["Principled BSDF"].inputs["Emission Color"].default_value = srgb(ORANGE)
rn["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
rn["Principled BSDF"].inputs["Alpha"].default_value = 0.75
waves = empty("waves", (0.95, S / 2 - T - 0.3, 1.5), room)
for i in range(4):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.45, minor_radius=0.02, rotation=(math.pi / 2, 0, 0))
    ring = bpy.context.object
    ring.data.materials.append(ring_mat)
    ring.parent = waves
    period = 40
    key(ring, 1, scale=(0.001,) * 3)
    f = open_at + 12 + i * 10
    key(ring, f - 1, scale=(0.001,) * 3)
    while f < end - 2:
        loud = f < shut_at
        grow = 1.6 if loud else 0.7
        key(ring, f, scale=(0.4,) * 3, location=(0, 0, 0))
        key(ring, f + period - 2, scale=(grow,) * 3, location=(0, -0.8 if loud else -0.25, 0))
        key(ring, f + period - 1, scale=(0.001,) * 3, location=(0, 0, 0))
        f += period

# ---------------------------------------------------------------- light: a warm afternoon
bpy.ops.object.light_add(type="SUN", location=(0, 0, 10))
sun = bpy.context.object
sun.data.energy, sun.data.angle = 3.2, math.radians(4)
sun.data.color = (1.0, 0.9, 0.78)
sun.rotation_euler = (math.radians(50), 0, math.radians(-145))
bpy.ops.object.light_add(type="AREA", location=(-6, -7, 8))
fill = bpy.context.object
fill.data.size, fill.data.energy = 10, 900
fill.rotation_euler = (math.radians(50), 0, math.radians(-40))

# The room turns a little, the way a camera breathes in those films.
key(room, 1, rotation_euler=(0, 0, math.radians(-6)))
key(room, end, rotation_euler=(0, 0, math.radians(4)))

bpy.ops.object.camera_add()
cam = bpy.context.object
scene.camera = cam
cam.data.type = "ORTHO"
cam.data.ortho_scale = 9.9
cam.rotation_euler = (math.radians(60), 0, math.radians(40))
bpy.context.view_layer.update()
forward = cam.matrix_world.to_3x3() @ Vector((0, 0, -1))
up = cam.matrix_world.to_3x3() @ Vector((0, 1, 0))
# Aim at the middle of the room, then slide the view up so the room sits in the lower part and the
# words have the top third.
cam.location = Vector((0, 0.2, 1.0)) - forward * 25 + up * 0.75

if os.environ.get("DEBUG"):
    cam.data.ortho_scale = 3.2
    cam.location = Vector(tuple(float(v) for v in os.environ.get("DEBUG_AT", "0.2,1.1,0.8").split(","))) - forward * 25
stills = os.environ.get("STILLS")
if stills:
    for f in [int(x) for x in stills.split(",")]:
        scene.frame_set(f)
        scene.render.filepath = OUT.rstrip("/") + f"/still_{f:04d}.jpg"
        bpy.ops.render.render(write_still=True)
else:
    bpy.ops.render.render(animation=True)
