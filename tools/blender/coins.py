"""A soft clay house with coins dropping beside it, one per cost on top of the price.

    blender -b -P tools/blender/coins.py -- <frames dir> [seconds] [coins]

Renders JPEG frames (1080x1920, 30 fps) with Eevee. tools/render.py lays the words over them, so the
scene leaves the top third clear. The look follows Airbnb's 3D illustrations: rounded, matte,
one big soft light, the app's violet and orange.
"""
import math
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else "/tmp/coins/"
SECONDS = float(argv[1]) if len(argv) > 1 else 10
COINS = int(argv[2]) if len(argv) > 2 else 6
FPS = 30


def srgb(hex_):
    """sRGB hex to the linear values Blender's colour inputs expect."""
    h = hex_.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


VIOLET, NIGHT, ORANGE, ORANGE_LIGHT, CREAM, PLUM = "#5A3EC0", "#34216F", "#F97316", "#FFAF5E", "#FFF4EC", "#7D3AA8"

# ---------------------------------------------------------------- empty scene
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
scene.view_settings.view_transform = "Standard"  # keep brand colours as they are
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 95  # a cached scene is about 100 MB as JPEG, 700 MB as PNG
scene.render.filepath = OUT.rstrip("/") + "/"


def material(name, hex_, rough=0.65):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = srgb(hex_)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def soften(obj, width=0.08, segments=5):
    mod = obj.modifiers.new("bevel", "BEVEL")
    mod.width, mod.segments = width, segments
    mod.limit_method = "ANGLE"
    for poly in obj.data.polygons:
        poly.use_smooth = True


def key(obj, frame, **values):
    for attr, value in values.items():
        setattr(obj, attr, value)
        obj.keyframe_insert(data_path=attr, frame=frame)


world = bpy.data.worlds.new("world")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = srgb(VIOLET)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.9

# ---------------------------------------------------------------- the backdrop: a floor that curves up
bpy.ops.mesh.primitive_plane_add(size=300, location=(0, 0, 0))
floor = bpy.context.object
floor.data.materials.append(material("floor", VIOLET, 0.85))

# ---------------------------------------------------------------- the house
house = bpy.data.objects.new("house", None)
scene.collection.objects.link(house)
house.location = (-1.1, 1.0, 0)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.75))
body = bpy.context.object
body.scale = (1.6, 1.4, 1.5)
bpy.ops.object.transform_apply(scale=True)
soften(body, 0.12)
body.data.materials.append(material("body", CREAM))
body.parent = house
bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=1.35, depth=1.0, location=(0, 0, 2.0), rotation=(0, 0, math.pi / 4))
roof = bpy.context.object
roof.scale = (1.0, 0.9, 1.0)
bpy.ops.object.transform_apply(scale=True)
soften(roof, 0.1)
roof.data.materials.append(material("roof", ORANGE))
roof.parent = house
for x in (-0.38, 0.38):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, -0.71, 0.95))
    win = bpy.context.object
    win.scale = (0.34, 0.06, 0.34)
    bpy.ops.object.transform_apply(scale=True)
    soften(win, 0.04)
    win.data.materials.append(material("window", PLUM))
    win.parent = house
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.71, 0.35))
door = bpy.context.object
door.scale = (0.34, 0.06, 0.62)
bpy.ops.object.transform_apply(scale=True)
soften(door, 0.05)
door.data.materials.append(material("door", ORANGE))
door.parent = house

# The house pops in: 0 → a little over → settled.
key(house, 1, scale=(0.01, 0.01, 0.01))
key(house, 10, scale=(1.08, 1.08, 1.08))
key(house, 16, scale=(1, 1, 1))

# ---------------------------------------------------------------- the coins
coin_mat, rim_mat = material("coin", ORANGE, 0.35), material("rim", ORANGE_LIGHT, 0.35)
h = 0.22
for i in range(COINS):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.62, depth=h, vertices=64, location=(1.5, 0.6, 0))
    coin = bpy.context.object
    soften(coin, 0.05, 4)
    coin.data.materials.append(coin_mat)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.62, minor_radius=0.04, location=(1.5, 0.6, h / 2))
    rim = bpy.context.object
    rim.data.materials.append(rim_mat)
    rim.parent = coin
    rim.location = (0, 0, h / 2)
    rest = h / 2 + i * (h + 0.01)
    start = 24 + i * 22
    wobble = (i % 2 * 2 - 1) * 0.12
    key(coin, 1, location=(1.5, 0.6, 40.0), rotation_euler=(wobble, 0, 0))  # out of the frame until its turn
    key(coin, start - 1, location=(1.5, 0.6, 40.0), rotation_euler=(wobble, 0, 0))
    key(coin, start, location=(1.5, 0.6, 7.0), rotation_euler=(wobble, 0, 0))
    key(coin, start + 9, location=(1.5 + (i % 3 - 1) * 0.03, 0.6, rest), rotation_euler=(0, 0, i * 0.3))
    key(coin, start + 12, location=(1.5 + (i % 3 - 1) * 0.03, 0.6, rest + 0.18), rotation_euler=(0, 0, i * 0.3))
    key(coin, start + 15, location=(1.5 + (i % 3 - 1) * 0.03, 0.6, rest), rotation_euler=(0, 0, i * 0.3))

# Two round bushes, so the scene reads as a place and not a diagram.
for (x, y, r) in [(-2.55, 0.4, 0.42), (-2.15, -0.1, 0.3)]:
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(x, y, r * 0.9), segments=48, ring_count=24)
    bush = bpy.context.object
    for poly in bush.data.polygons:
        poly.use_smooth = True
    bush.data.materials.append(material("bush", ORANGE_LIGHT))
    key(bush, 1, scale=(0.01, 0.01, 0.01))
    key(bush, 14, scale=(1.1, 1.1, 1.1))
    key(bush, 20, scale=(1, 1, 1))

# A soft orange disc on the floor under everything, like the flat cards.
bpy.ops.mesh.primitive_cylinder_add(radius=3.2, depth=0.02, vertices=128, location=(0.2, 0.8, 0.01))
bpy.context.object.data.materials.append(material("disc", ORANGE, 0.9))

# ---------------------------------------------------------------- light and camera
bpy.ops.object.light_add(type="AREA", location=(-4, -5, 8))
light = bpy.context.object
light.data.size = 8
light.data.energy = 2200
light.rotation_euler = (math.radians(50), 0, math.radians(-35))
bpy.ops.object.light_add(type="AREA", location=(5, -3, 3))
fill = bpy.context.object
fill.data.size = 6
fill.data.energy = 500
fill.data.color = srgb(ORANGE_LIGHT)[:3]
fill.rotation_euler = (math.radians(70), 0, math.radians(55))

bpy.ops.object.camera_add()
cam = bpy.context.object
scene.camera = cam
cam.data.lens = 48
target = bpy.data.objects.new("target", None)
scene.collection.objects.link(target)
target.location = (0.2, 2.6, 0.2)  # aiming past the objects puts them in the lower part of the frame
track = cam.constraints.new("TRACK_TO")
track.target = target
track.track_axis, track.up_axis = "TRACK_NEGATIVE_Z", "UP_Y"
end = scene.frame_end
key(cam, 1, location=(-1.2, -9.5, 13.0))
key(cam, end, location=(1.2, -8.6, 12.2))
for fc in cam.animation_data.action.fcurves if cam.animation_data and getattr(cam.animation_data.action, "fcurves", None) else []:
    for kp in fc.keyframe_points:
        kp.interpolation = "SINE"

import os

stills = os.environ.get("STILLS")  # e.g. "1,60,300": render only these frames, to check a layout
if stills:
    for f in [int(x) for x in stills.split(",")]:
        scene.frame_set(f)
        scene.render.filepath = OUT.rstrip("/") + f"/still_{f:04d}.jpg"
        bpy.ops.render.render(write_still=True)
else:
    bpy.ops.render.render(animation=True)
