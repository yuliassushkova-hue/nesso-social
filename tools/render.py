#!/usr/bin/env python3
"""Render a week of Reels, carousels and Stories from weeks/<monday>.py (a list ITEMS) into posts/.

    python3 tools/render.py weeks/2026-11-02.py              # everything
    python3 tools/render.py weeks/2026-11-02.py r-check-01   # only these ids

Needs Pillow (`python3 -m venv .venv && .venv/bin/pip install pillow`) and macOS (the H.264 encoder is
tools/frames-to-mp4.swift, compiled on first use). Each item becomes posts/<date>-<channel>-<slug>/
with its media and a post.md, so the week is reviewed as one pull request.

The look is the app's two loud colours: Nesso orange and the measurement card's violet, full
bleed, each with a big disc of the other. `*word*` puts a word on a marker of the other colour.
A Reel is a list of cards; each rises in and holds, and a bar at the top shows how far through the
viewer is. Words stay inside Instagram's safe area (clear of the top bar, the caption and the
buttons on the right).
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = str(ROOT / "assets/fonts/PlusJakartaSans-Variable.ttf")
ENCODER_SRC = ROOT / "tools/frames-to-mp4.swift"
ENCODER = ROOT / "tools/.frames-to-mp4"
W, H, SH, FPS = 1080, 1920, 1350, 30
LEFT, RIGHT = 96, 920  # clear of the Reel buttons on the right
TOP, BOTTOM = 300, 1440  # clear of the top bar and the caption

# The app's own colours (nesso_mobile src/lib/tokens.ts).
ORANGE, ORANGE_STRONG, ORANGE_LIGHT = (249, 115, 22), (234, 106, 16), (255, 175, 94)
VIOLET, PLUM, NIGHT, BLUSH = (90, 62, 192), (125, 58, 168), (52, 33, 111), (226, 124, 176)
INK, WHITE, CREAM = (22, 24, 28), (255, 255, 255), (255, 247, 239)

THEMES = {
    # the app's orange (#F97316), flat, with white type; the marker and the button are violet
    "orange": dict(stops=[ORANGE, ORANGE], glow=None, disc=VIOLET, fg=WHITE, soft=WHITE,
                   big=WHITE, hl=VIOLET, hl_fg=WHITE, pill=VIOLET, pill_fg=WHITE, label=WHITE),
    # white type on violet; the marker is orange with ink type
    "violet": dict(stops=[VIOLET, PLUM, NIGHT], glow=BLUSH, disc=ORANGE, fg=WHITE, soft=(236, 228, 255),
                   big=ORANGE_LIGHT, hl=ORANGE, hl_fg=INK, pill=ORANGE, pill_fg=INK, label=ORANGE_LIGHT),
    # the deepest violet, for answers and endings
    "night": dict(stops=[NIGHT, VIOLET], glow=PLUM, disc=ORANGE, fg=WHITE, soft=(226, 220, 250),
                  big=ORANGE_LIGHT, hl=ORANGE, hl_fg=INK, pill=ORANGE, pill_fg=INK, label=ORANGE_LIGHT),
}

_fonts = {}


def font(size, weight=700):
    key = (size, weight)
    if key not in _fonts:
        f = ImageFont.truetype(FONT, size)
        f.set_variation_by_axes([weight])
        _fonts[key] = f
    return _fonts[key]


def ground(theme, height=H):
    """Diagonal gradient through the theme's stops, a soft glow top right, a disc of the other colour."""
    t = THEMES[theme]
    small = Image.new("RGB", (W // 8, height // 8))
    px = small.load()
    stops = t["stops"]
    for y in range(small.height):
        for x in range(small.width):
            u = min(1, max(0, (0.35 * x / small.width + 0.65 * y / small.height)))
            seg = u * (len(stops) - 1)
            i = min(int(seg), len(stops) - 2)
            f = seg - i
            px[x, y] = tuple(round(a + (b - a) * f) for a, b in zip(stops[i], stops[i + 1]))
    img = small.resize((W, height), Image.BICUBIC).convert("RGBA")
    if t["glow"]:
        glow = Image.new("RGBA", (W, height), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([W - 500, -300, W + 400, 520], fill=t["glow"] + (150,))
        img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(120)))
    disc = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    r = 470 if height == H else 300
    cy = height - 330 if height == H else height + 20
    ImageDraw.Draw(disc).ellipse([W - r - 40, cy - r, W + r - 40, cy + r], fill=t["disc"] + (255,))
    img.alpha_composite(disc)
    return img.convert("RGB")


def tokens(text):
    """Split text into words; each word is a list of (piece, is_marked). `*...*` marks, and may
    start or end inside a word (l'*umidità*?)."""
    out, marked = [], False
    for para_i, para in enumerate(text.split("\n")):
        if para_i:
            out.append(None)
        for word in para.split(" "):
            if not word:
                continue
            pieces, buf = [], ""
            for ch in word:
                if ch == "*":
                    if buf:
                        pieces.append((buf, marked))
                    buf, marked = "", not marked
                else:
                    buf += ch
            if buf:
                pieces.append((buf, marked))
            if pieces:
                out.append(pieces)
    return out


def word_len(f, pieces):
    return sum(f.getlength(t) for t, _ in pieces)


def wrap(text, f, width):
    lines, line, line_w = [], [], 0
    space = f.getlength(" ")
    for pieces in tokens(text):
        if pieces is None:
            lines.append(line)
            line, line_w = [], 0
            continue
        ww = word_len(f, pieces)
        if line and line_w + space + ww > width:
            lines.append(line)
            line, line_w = [], 0
        line_w += (space if line else 0) + ww
        line.append(pieces)
    if line:
        lines.append(line)
    return lines


def draw_text(d, text, f, y, t, color=None, width=RIGHT - LEFT, leading=1.18, marker=True):
    """Draw wrapped text; marked pieces sit on a rounded marker in the other colour."""
    color = color or t["fg"]
    step = round(f.size * leading)
    space = f.getlength(" ")
    for line in wrap(text, f, width):
        # One marker per run of marked pieces on a line, so "*due rubinetti*" is one block.
        pad = round(f.size * 0.16)
        x, runs, prev = LEFT, [], False
        for pieces in line:
            for piece, mark in pieces:
                m = mark and marker
                if m and not prev:
                    x += pad
                if prev and not m:
                    x += pad
                w = f.getlength(piece)
                if m:
                    if prev:
                        runs[-1][1] = x + w
                    else:
                        runs.append([x, x + w])
                prev = m
                x += w
            x += space
        top_, bottom_ = f.getbbox("Hg")[1], f.getbbox("Hg")[3]
        for a, b in runs:
            d.rounded_rectangle([a - pad + 4, y + top_ - 10, b + pad - 4, y + bottom_ + 12], radius=round(f.size * 0.22), fill=t["hl"])
        x, prev = LEFT, False
        for pieces in line:
            for piece, mark in pieces:
                m = mark and marker
                if m != prev:
                    x += pad
                d.text((x, y), piece, font=f, fill=t["hl_fg"] if m else color)
                x += f.getlength(piece)
                prev = m
            x += space
        y += step
    return y


def chip(d, text, x, y, t, size=40, fill=None, fg=None):
    f = font(size, 800)
    w = f.getlength(text) + 2 * round(size * 0.9)
    h = round(size * 2.1)
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill or t["pill"])
    d.text((x + round(size * 0.9), y + round(size * 0.48)), text, font=f, fill=fg or t["pill_fg"])
    return y + h


def card_layer(card, series, theme, zone=(TOP, BOTTOM)):
    """The card's words on a transparent layer, laid out once and centred in the safe area."""
    t = THEMES[theme]
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    if series:
        d.text((LEFT, 210), series.upper(), font=font(36, 800), fill=t["label"])
    body = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    b = ImageDraw.Draw(body)
    kind, y = card["kind"], 0
    if kind == "hook":
        y = draw_text(b, card["text"], font(card.get("size", 120), 800), y, t, leading=1.12)
        if card.get("sub"):
            y = draw_text(b, card["sub"], font(54, 600), y + 50, t, color=t["soft"])
    elif kind == "step":
        n = str(card["n"])
        b.ellipse([LEFT, 0, LEFT + 160, 160], fill=t["hl"])
        fn = font(92, 800)
        b.text((LEFT + 80 - fn.getlength(n) / 2, 20), n, font=fn, fill=t["hl_fg"])
        y = draw_text(b, card["text"], font(card.get("size", 96), 800), 230, t, leading=1.1)
        if card.get("sub"):
            y = draw_text(b, card["sub"], font(48, 600), y + 36, t, color=t["soft"])
    elif kind == "note":
        y = chip(b, card.get("label", "Cosa non stabilisce").upper(), LEFT, 0, t, size=38, fill=t["hl"], fg=t["hl_fg"])
        y = draw_text(b, card["text"], font(card.get("size", 74), 700), y + 50, t, leading=1.16)
    elif kind == "big":
        if card.get("over"):
            y = draw_text(b, card["over"], font(58, 700), y, t, color=t["soft"]) + 20
        y = draw_text(b, card["text"], font(card.get("size", 200), 800), y, t, color=t["big"], leading=1.0)
        if card.get("sub"):
            y = draw_text(b, card["sub"], font(62, 700), y + 30, t, leading=1.16)
    elif kind == "answer":
        y = chip(b, card.get("label", "LA RICERCA"), LEFT, 0, t, size=42, fill=t["hl"], fg=t["hl_fg"])
        y = draw_text(b, card["text"], font(card.get("size", 78), 700), y + 50, t, leading=1.18)
        if card.get("source"):
            y = draw_text(b, card["source"], font(38, 600), y + 50, t, color=t["soft"])
    elif kind == "cta":
        y = draw_text(b, card["text"], font(card.get("size", 104), 800), y, t, leading=1.08)
        y = chip(b, card.get("button", "Link in bio"), LEFT, y + 60, t, size=54)
        b.text((LEFT, y + 40), card.get("site", "nesso.fit"), font=font(52, 800), fill=t["soft"])
        y += 110
    elif kind == "fact":
        if card.get("label"):
            y = chip(b, card["label"], LEFT, 0, t, size=40, fill=t["hl"], fg=t["hl_fg"]) + 50
        y = draw_text(b, card["text"], font(card.get("size", 92), 800), y, t, leading=1.1)
        if card.get("sub"):
            y = draw_text(b, card["sub"], font(52, 600), y + 40, t, color=t["soft"], leading=1.22)
        if card.get("source"):
            y = draw_text(b, card["source"], font(38, 600), y + 50, t, color=t["soft"])
    elif kind == "serif":
        # A word or two at a time, centred, in the landing page's serif: the warm-interior film style.
        reg = ImageFont.truetype(str(ROOT / "assets/fonts/InstrumentSerif-Regular.ttf"), card.get("size", 150))
        ita = ImageFont.truetype(str(ROOT / "assets/fonts/InstrumentSerif-Italic.ttf"), card.get("size", 150))
        cream, glow = (255, 244, 226), (30, 14, 6, 235)
        lines = card["text"].split("\n")
        lh = round(reg.size * 1.02)
        y = 220  # room above for the halo; the same is added below, so the block stays centred
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        words = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wd = ImageDraw.Draw(words)
        for li, line in enumerate(lines):
            pieces = [(t, i % 2 == 1) for i, t in enumerate(line.split("*")) if t]
            total = sum((ita if it else reg).getlength(t) for t, it in pieces)
            x = (W - total) / 2
            for t, it in pieces:
                f = ita if it else reg
                sd.text((x, y + li * lh), t, font=f, fill=glow)
                wd.text((x, y + li * lh), t, font=f, fill=(255, 196, 140) if it else cream)
                x += f.getlength(t)
        # a soft warm-dark halo behind the words, so they read on a white door as well as on a lamp
        halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(halo).ellipse([40, y - 150, W - 40, y + lh * len(lines) + 150], fill=(25, 12, 5, 95))
        body.alpha_composite(halo.filter(ImageFilter.GaussianBlur(90)))
        body.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(14)))
        body.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(4)))
        body.alpha_composite(words)
        y += lh * len(lines)
        if card.get("sub"):
            fs = font(card.get("sub_size", 44), 700)
            subw = fs.getlength(card["sub"])
            b.text(((W - subw) / 2, y + 30), card["sub"], font=fs, fill=cream)
            y += 30 + fs.size
        y += 220
    elif kind == "brand":
        # the real mark over footage, white word, orange pin and o, with a soft dark halo behind
        wm = wordmark(card.get("height", 150), WHITE)
        y = 220
        halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(halo).ellipse([60, y - 140, W - 60, y + wm.height + 260], fill=(20, 10, 4, 120))
        body.alpha_composite(halo.filter(ImageFilter.GaussianBlur(90)))
        body.alpha_composite(wm, ((W - wm.width) // 2, y))
        y += wm.height + 40
        if card.get("sub"):
            fs = font(card.get("sub_size", 48), 700)
            b.text(((W - fs.getlength(card["sub"])) / 2, y), card["sub"], font=fs, fill=WHITE)
            y += fs.size
        y += 220
    elif kind == "caption":
        # Words on solid blocks, one block per line, the way captions sit on a feed video:
        # readable on any footage without darkening it.
        styles = {"white": (WHITE, INK), "violet": (VIOLET, WHITE), "orange": (ORANGE, WHITE), "ink": (INK, WHITE)}
        for blk in card["blocks"]:
            f = font(blk.get("size", 104), 800)
            fill, fg = styles[blk.get("style", "white")]
            pad_x, pad_y = round(f.size * 0.32), round(f.size * 0.16)
            for line in wrap(blk["text"].replace("*", ""), f, RIGHT - LEFT - 2 * pad_x):
                words = " ".join("".join(p for p, _ in w) for w in line)
                w = f.getlength(words)
                top_, bottom_ = f.getbbox("Hg")[1], f.getbbox("Hg")[3]
                h = bottom_ - top_
                x0 = LEFT if card.get("align") != "center" else (W - w) / 2 - pad_x
                b.rounded_rectangle([x0, y, x0 + w + 2 * pad_x, y + h + 2 * pad_y], radius=round(f.size * 0.2), fill=fill)
                b.text((x0 + pad_x, y + pad_y - top_), words, font=f, fill=fg)
                y += h + 2 * pad_y + 10
            y += 22
    else:
        raise ValueError(f"unknown card kind {kind}")
    if card.get("phone"):
        # The real app screen rises into the lower half of the frame.
        phone = phone_crop(card["phone"])
        ph = card.get("phone_height", 1060)
        phone = phone.resize((round(phone.width * ph / phone.height), ph), Image.LANCZOS)
        tilted = phone.rotate(card.get("phone_tilt", -5), resample=Image.BICUBIC, expand=True)
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        px0, py0 = (W - tilted.width) // 2 + card.get("phone_dx", 60), card.get("phone_top", 860)
        ImageDraw.Draw(shadow).rounded_rectangle([px0 + 30, py0 + 40, px0 + tilted.width, py0 + tilted.height], radius=90, fill=(20, 10, 40, 120))
        layer.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(35)))
        layer.paste(tilted, (px0, py0), tilted)
    if kind == "caption" or card.get("text_top"):
        offset = card.get("y", 330) if kind == "caption" else card.get("text_y", 0)
        layer.alpha_composite(body.crop((0, 0, W, H - offset)), (0, offset))
        return layer
    offset = zone[0] + max(0, (zone[1] - zone[0] - y) // 2) - (60 if zone == (TOP, BOTTOM) else 0)
    layer.alpha_composite(body.crop((0, 0, W, H - offset)), (0, offset))
    return layer


def pin_image(height):
    """The Nesso pin from its own geometry (a 24x34 box, a hole of r=4.6 at the centre of the head)."""
    s = height / 34
    im = Image.new("RGBA", (round(24 * s), round(34 * s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([0, 0, 24 * s, 24 * s], fill=ORANGE)
    d.polygon([(1.2 * s, 16.5 * s), (22.8 * s, 16.5 * s), (12 * s, 34 * s)], fill=ORANGE)
    d.ellipse([(12 - 4.6) * s, (12 - 4.6) * s, (12 + 4.6) * s, (12 + 4.6) * s], fill=(0, 0, 0, 0))
    return im


def wordmark(height, word=INK):
    """The app's lockup: the orange pin, then "Ness" in the word colour and the "o" in orange.
    The word is ink on light grounds and white on footage, the way the app places it."""
    f = font(round(height * 0.92), 700)
    p = pin_image(height)
    gap = round(height * 0.34)
    w = p.width + gap + f.getlength("Nesso")
    im = Image.new("RGBA", (round(w) + 4, height + 20), (0, 0, 0, 0))
    im.alpha_composite(p, (0, 10))
    d = ImageDraw.Draw(im)
    x = p.width + gap
    d.text((x, 10 + height * 0.02), "Ness", font=f, fill=word)
    d.text((x + f.getlength("Ness"), 10 + height * 0.02), "o", font=f, fill=ORANGE)
    return im


def ease(t):
    return 1 - (1 - t) ** 3


def progress(d, cards, i, frac, theme):
    t = THEMES[theme]
    n = len(cards)
    gap, x0, x1, y = 12, 60, W - 60, 120
    seg = (x1 - x0 - gap * (n - 1)) / n
    off = t["fg"] + (70,)
    for k in range(n):
        a = x0 + k * (seg + gap)
        d.rounded_rectangle([a, y, a + seg, y + 9], radius=4, fill=off)
        fill = 1.0 if k < i else (frac if k == i else 0)
        if fill > 0:
            d.rounded_rectangle([a, y, a + seg * fill, y + 9], radius=4, fill=t["fg"])


def encoder():
    if not ENCODER.exists():
        subprocess.run(["swiftc", "-O", "-o", str(ENCODER), str(ENCODER_SRC)], check=True)
    return ENCODER


def card_theme(item, card):
    return card.get("theme", item.get("theme", "violet"))


BLENDER = "/Applications/Blender.app/Contents/MacOS/Blender"


CACHE = ROOT / "tools/.cache"


def blender_frames(spec, total_frames):
    """Render a 3D scene from tools/blender/ to frames, cached by the script, its arguments and the
    length, so changing the words over a scene does not render it again."""
    import hashlib
    script = ROOT / "tools/blender" / spec["script"]
    args = [str(a) for a in spec.get("args", [])]
    seconds = total_frames / FPS
    digest = hashlib.sha256((script.read_text() + repr(args) + f"{seconds:.3f}").encode()).hexdigest()[:12]
    out = CACHE / f"{script.stem}-{digest}"
    frames = sorted(out.glob("*.jpg"))
    if len(frames) < total_frames:
        out.mkdir(parents=True, exist_ok=True)
        cmd = [BLENDER, "-b", "-P", str(script), "--", str(out), f"{seconds:.3f}", *args]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        frames = sorted(out.glob("*.jpg"))
    return None, frames


CLIP_TOOL_SRC = ROOT / "tools/clip-frames.swift"
CLIP_TOOL = ROOT / "tools/.clip-frames"


def clip_frames(clips, total_frames):
    """Real footage, cut and centre-cropped to 1080x1920 at 30 fps, one clip after another.
    Each clip is {"file": path, "start": seconds, "secs": seconds}; the last one runs to the end."""
    if not CLIP_TOOL.exists():
        subprocess.run(["swiftc", "-O", "-o", str(CLIP_TOOL), str(CLIP_TOOL_SRC)], check=True)
    out = Path(tempfile.mkdtemp())
    index = 1
    for i, clip in enumerate(clips):
        frames = round(clip["secs"] * FPS) if i < len(clips) - 1 else total_frames - (index - 1)
        if frames <= 0:
            break
        subprocess.run([str(CLIP_TOOL), str(Path(clip["file"]).expanduser()), str(clip.get("start", 0)),
                        f"{frames / FPS:.4f}", str(out), str(index)], check=True)
        index += frames
    return out, sorted(out.glob("*.jpg"))


def scrim(theme):
    """A wash of the theme's deep colour over the top of real footage, so white words read on it."""
    t = THEMES[theme]
    deep = t["stops"][-1] if theme != "orange" else NIGHT
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for y in range(0, 1250):
        a = round(215 * max(0.0, 1 - y / 1250) ** 1.3)
        d.line([(0, y), (W, y)], fill=deep + (a,))
    return layer


def render_reel(item, out):
    cards = item["cards"]
    grounds, frames = {}, Path(tempfile.mkdtemp())
    n = 0
    total_frames = sum(round(c.get("secs", 2.5) * FPS) for c in cards)
    scene_dir, scene = (None, None)
    if item.get("blender"):
        scene_dir, scene = blender_frames(item["blender"], total_frames)
    if item.get("clips"):
        scene_dir, scene = clip_frames(item["clips"], total_frames)
    wash = scrim(item.get("theme", "violet")) if item.get("clips") and item.get("wash") else None
    zone = tuple(item.get("text_zone", (TOP, BOTTOM)))
    try:
        for i, card in enumerate(cards):
            theme = card_theme(item, card)
            if theme not in grounds:
                grounds[theme] = ground(theme).convert("RGBA")
            base = grounds[theme]
            layer = card_layer(card, item.get("series"), theme, zone)
            total = round(card.get("secs", 2.5) * FPS)
            fade = round(0.3 * FPS)
            for f in range(total):
                e = ease(min(1, f / fade))
                frame = Image.open(scene[min(n, len(scene) - 1)]).convert("RGBA") if scene else base.copy()
                if wash is not None:
                    frame.alpha_composite(wash)
                moved = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                moved.paste(layer, (0, round(70 * (1 - e))))
                if e < 1:
                    moved.putalpha(moved.getchannel("A").point(lambda v: round(v * e)))
                frame.alpha_composite(moved)
                if item.get("progress", True):
                    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                    progress(ImageDraw.Draw(overlay), cards, i, f / max(1, total - 1), theme)
                    frame.alpha_composite(overlay)
                n += 1
                frame.convert("RGB").save(frames / f"{n:05d}.png", compress_level=1)
        subprocess.run([str(encoder()), str(frames), str(FPS), str(out)], check=True, stdout=subprocess.DEVNULL)
    finally:
        shutil.rmtree(frames)
        if scene_dir:
            shutil.rmtree(scene_dir)
    return n / FPS


def render_story(item, out):
    theme = card_theme(item, item["card"])
    img = ground(theme).convert("RGBA")
    img.alpha_composite(card_layer(item["card"], item.get("series"), theme))
    img.convert("RGB").save(out, "JPEG", quality=90)


def slide_theme(item, slide, index):
    """Slides alternate the two colours, so a swipe always changes the screen."""
    if "theme" in slide:
        return slide["theme"]
    first = item.get("theme", "orange")
    other = "violet" if first == "orange" else "orange"
    return first if index % 2 == 1 else other


def render_slide(slide, item, index, total, out):
    theme = slide_theme(item, slide, index)
    t = THEMES[theme]
    img = ground(theme, SH).convert("RGBA")
    d = ImageDraw.Draw(img)
    d.text((LEFT, 80), item.get("series", "").upper(), font=font(34, 800), fill=t["label"])
    counter = f"{index}/{total}"
    fc = font(34, 800)
    d.text((W - LEFT - fc.getlength(counter), 80), counter, font=fc, fill=t["fg"])
    width = W - 2 * LEFT
    layer = Image.new("RGBA", (W, SH), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    y = 0
    if slide.get("big"):
        if slide.get("over"):
            y = draw_text(ld, slide["over"], font(52, 700), y, t, color=t["soft"], width=width) + 10
        y = draw_text(ld, slide["big"], font(slide.get("big_size", 220), 800), y, t, color=t["big"], width=width, leading=1.0)
        y += 24
    if slide.get("text"):
        size = slide.get("size", 92 if index == 1 else 76)
        y = draw_text(ld, slide["text"], font(size, 800), y, t, width=width, leading=1.12)
    if slide.get("sub"):
        y = draw_text(ld, slide["sub"], font(slide.get("sub_size", 48), 600), y + 34, t, color=t["soft"], width=width, leading=1.25)
    if slide.get("button"):
        y = chip(ld, slide["button"], LEFT, y + 50, t, size=50)
        ld.text((LEFT, y + 30), "nesso.fit", font=font(46, 800), fill=t["soft"])
        y += 90
    room_top = 170
    if slide.get("photo"):
        # The whole phone sits under the words, as large as the room left allows.
        offset = room_top
        photo_top = offset + y + 50
        ph = max(420, SH - photo_top - 30)
        phone = phone_crop(slide["photo"])
        phone = phone.resize((round(phone.width * ph / phone.height), ph), Image.LANCZOS)
        tilted = phone.rotate(-4, resample=Image.BICUBIC, expand=True)
        x0 = (W - tilted.width) // 2 + 40
        shadow = Image.new("RGBA", (W, SH), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle([x0 + 30, photo_top + 30, x0 + tilted.width + 10, photo_top + tilted.height], radius=80, fill=(20, 10, 40, 110))
        img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(30)))
        img.paste(tilted, (x0, photo_top), tilted)
    else:
        offset = max(room_top, room_top + (SH - 150 - room_top - y) // 2)
    img.alpha_composite(layer.crop((0, 0, W, SH - offset)), (0, offset))
    d = ImageDraw.Draw(img)
    if slide.get("source"):
        d.text((LEFT, SH - 100), slide["source"], font=font(30, 700), fill=t["fg"])
    if index == 1 and total > 1:
        hint = "Scorri  →"
        fh = font(40, 800)
        bw = fh.getlength(hint) + 70
        d.rounded_rectangle([W - LEFT - bw, SH - 140, W - LEFT, SH - 60], radius=40, fill=WHITE)
        d.text((W - LEFT - bw + 35, SH - 125), hint, font=fh, fill=INK)
    img.convert("RGB").save(out, "JPEG", quality=92)


def pad_screen(src, out):
    """A tall app mockup (1290x2796) widened to 9:16 by stretching its edge colours, then 1080x1920."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target = round(h * 9 / 16)
    pad = (target - w) // 2
    canvas = Image.new("RGB", (target, h))
    canvas.paste(im, (pad, 0))
    canvas.paste(im.crop((0, 0, 1, h)).resize((pad, h)), (0, 0))
    canvas.paste(im.crop((w - 1, 0, w, h)).resize((target - w - pad, h)), (pad + w, 0))
    canvas.resize((W, H), Image.LANCZOS).save(out, "JPEG", quality=90)


SH = 1350  # a carousel slide is 4:5


def phone_crop(src):
    """The phone out of a framed app mockup (1290x2796, phone from about y=760 down)."""
    im = Image.open(Path(src).expanduser()).convert("RGB")
    w, h = im.size
    phone = im.crop((round(w * 0.137), round(h * 0.2725), round(w * 0.865), round(h * 0.9845))).convert("RGBA")
    mask = Image.new("L", phone.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, phone.width - 1, phone.height - 1], radius=round(phone.width * 0.13), fill=255)
    phone.putalpha(mask)
    return phone


def post_md(item, media, kind):
    caption = item.get("caption", "").strip()
    head = f"---\nchannel: {item['channel']}\nat: {item['at']}\ntype: {kind}\nmedia: {media}\n---\n"
    return head + (caption + "\n" if caption else "")


def main(argv):
    source = Path(argv[0])
    if source.suffix == ".py":
        import runpy
        spec = {"items": runpy.run_path(str(source))["ITEMS"]}
    else:
        spec = json.loads(source.read_text(encoding="utf-8"))
    only = set(argv[1:])
    for item in spec["items"]:
        if only and item["id"] not in only:
            continue
        folder = ROOT / "posts" / f"{item['at'][:10]}-{item['channel']}-{item['slug']}"
        folder.mkdir(parents=True, exist_ok=True)
        kind = item["type"]
        if kind == "carousel":
            for old in folder.glob("*.jpg"):
                old.unlink()
            names = []
            for i, slide in enumerate(item["slides"], 1):
                name = f"{i:02d}.jpg"
                render_slide(slide, item, i, len(item["slides"]), folder / name)
                names.append(name)
            media, note = ", ".join(names), f"{len(names)} slides"
        elif kind == "reel" and "scenes" in item:
            import audio
            import chat  # chat stories: tools/chat.py
            media = "reel.mp4"
            secs = chat.render_story(item, folder / media)
            audio.mux(folder / media, audio.mix(secs, item.get("music", "music-happy-home"), 0.22, item.get("music_start", 2.0), chat.sound_events(item)))
            note = f"{secs:.1f}s chat, with sound"
        elif kind == "reel" and "video" in item:
            media = "reel.mp4"
            shutil.copyfile(Path(item["video"]).expanduser(), folder / media)
            note = "copied"
        elif kind == "reel":
            media = "reel.mp4"
            secs = render_reel(item, folder / media)
            note = f"{secs:.1f}s"
            if item.get("music"):
                import audio
                audio.mux(folder / media, audio.mix(secs, item["music"], item.get("music_gain", 0.55), item.get("music_start", 0.0)))
                note += ", with music"
        elif "screen" in item:
            media = "story.jpg"
            pad_screen(Path(item["screen"]).expanduser(), folder / media)
            note = "screen"
        else:
            media = "story.jpg"
            render_story(item, folder / media)
            note = "card"
        (folder / "post.md").write_text(post_md(item, media, kind), encoding="utf-8")
        print(f"{item['id']}  {folder.name}  {note}")


if __name__ == "__main__":
    main(sys.argv[1:])
