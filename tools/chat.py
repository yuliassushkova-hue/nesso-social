"""Chat-story Reels, after Airbnb Italia's "Non preoccuparti." film: a real room, a message
anyone has received, a reply, then the line and the app.

    python3 tools/chat.py weeks/<file>.py <id> [out.mp4]

A story is a list of scenes:
  {"kind": "photo", "secs", "clip": {"file", "start"}, "bubble": "text", "who": "Marco"}
      real footage full-bleed, one message floating over it
  {"kind": "chat", "secs", "who", "role", "messages": [{"at", "from": "them"|"me", "text"|"photo", "typing"}]}
      a white chat thread; messages pop in at their time, "typing" dots before theirs
  {"kind": "headline", "secs", "text", "sub", "phone"}
      white, one big line, optionally the real app screen rising
  {"kind": "end", "secs", "line", "cta"}
      the Nesso mark
Emoji are drawn from the system's colour emoji font.
"""
import os
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render  # noqa: E402

W, H, FPS = render.W, render.H, render.FPS
INK, WHITE, ORANGE, VIOLET = render.INK, render.WHITE, render.ORANGE, render.VIOLET
GREY_BUBBLE, MUTED, LINE = (241, 241, 243), (120, 122, 128), (230, 230, 233)
EMOJI_FONT = "/System/Library/Fonts/Apple Color Emoji.ttc"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️‍]+")
_emoji_cache = {}


def emoji_image(ch, size):
    key = (ch, size)
    if key not in _emoji_cache:
        f = ImageFont.truetype(EMOJI_FONT, 160)
        im = Image.new("RGBA", (220, 220), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 10), ch, font=f, embedded_color=True)
        im = im.crop(im.getbbox() or (0, 0, 1, 1))
        s = size / 150
        _emoji_cache[key] = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    return _emoji_cache[key]


def runs(text):
    out, pos = [], 0
    for m in EMOJI.finditer(text):
        if m.start() > pos:
            out.append((text[pos:m.start()], False))
        out.append((m.group(0), True))
        pos = m.end()
    if pos < len(text):
        out.append((text[pos:], False))
    return out


def rich_len(text, f):
    return sum(f.size * 1.1 if e else f.getlength(t) for t, e in runs(text))


def wrap_rich(text, f, width):
    lines, line = [], ""
    for word in text.split(" "):
        cand = (line + " " + word).strip()
        if line and rich_len(cand, f) > width:
            lines.append(line)
            line = word
        else:
            line = cand
    if line:
        lines.append(line)
    return lines


def draw_rich(img, x, y, text, f, fill):
    d = ImageDraw.Draw(img)
    for t, e in runs(text):
        if e:
            em = emoji_image(t, f.size)
            img.alpha_composite(em, (round(x), round(y + f.size * 0.12)))
            x += f.size * 1.1
        else:
            d.text((x, y), t, font=f, fill=fill)
            x += f.getlength(t)


def bubble(text, mine, f=None, maxw=720, photo=None):
    """One message as an RGBA image."""
    f = f or render.font(56, 600)
    if photo is not None:
        ph = photo.copy()
        # a landscape crop out of the middle, the shape a phone photo takes in a thread
        tw, th = 680, 510
        scale = max(tw / ph.width, th / ph.height)
        ph = ph.resize((round(ph.width * scale), round(ph.height * scale)), Image.LANCZOS)
        left, top = (ph.width - tw) // 2, (ph.height - th) // 2
        ph = ph.crop((left, top, left + tw, top + th))
        mask = Image.new("L", ph.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, ph.width - 1, ph.height - 1], radius=40, fill=255)
        out = Image.new("RGBA", ph.size, (0, 0, 0, 0))
        out.paste(ph.convert("RGBA"), (0, 0), mask)
        return out
    lines = wrap_rich(text, f, maxw - 80)
    lh = round(f.size * 1.3)
    w = max(rich_len(line, f) for line in lines) + 76
    h = lh * len(lines) + 52
    im = Image.new("RGBA", (round(w), h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, im.width - 1, h - 1], radius=46, fill=VIOLET if mine else GREY_BUBBLE)
    for i, line in enumerate(lines):
        draw_rich(im, 38, 22 + i * lh, line, f, WHITE if mine else INK)
    return im


def typing_bubble(t):
    im = Image.new("RGBA", (190, 104), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 189, 103], radius=46, fill=GREY_BUBBLE)
    for i in range(3):
        phase = (t * 3 - i * 0.25) % 1
        lift = 10 * max(0, 1 - abs(phase - 0.3) * 4)
        cx, cy = 52 + i * 43, 52 - lift
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(160, 160, 166))
    return im


def avatar(name, size, color):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([0, 0, size - 1, size - 1], fill=color)
    f = render.font(round(size * 0.45), 800)
    ch = name[0].upper()
    d.text(((size - f.getlength(ch)) / 2, size * 0.22), ch, font=f, fill=WHITE)
    return im


def pop(im, k):
    """Scale-and-fade arrival for a bubble, k in 0..1."""
    e = 1 - (1 - min(1, max(0, k))) ** 3
    if e >= 1:
        return im
    s = 0.86 + 0.14 * e
    out = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    out.putalpha(out.getchannel("A").point(lambda v: round(v * e)))
    return out


def wordmark(height):
    return render.wordmark(height, INK)


def clip_frames(clip, frames):
    out = Path(tempfile.mkdtemp())
    subprocess.run([str(render.CLIP_TOOL), str(Path(clip["file"]).expanduser()), str(clip.get("start", 0)),
                    f"{frames / FPS:.4f}", str(out), "1"], check=True)
    return out, sorted(out.glob("*.jpg"))


def phone_image(path, height):
    p = render.phone_crop(path)
    return p.resize((round(p.width * height / p.height), height), Image.LANCZOS)


def scene_frames(sc, tmp_dirs):
    n = round(sc["secs"] * FPS)
    kind = sc["kind"]
    if kind == "photo":
        d, frames = clip_frames(sc["clip"], n)
        tmp_dirs.append(d)
        b = bubble(sc["bubble"], False, render.font(58, 650), maxw=880)
        av = avatar(sc.get("who", "?"), 96, sc.get("color", VIOLET))
        for i in range(n):
            t = i / FPS
            img = Image.open(frames[min(i, len(frames) - 1)]).convert("RGBA")
            k = (t - 0.25) / 0.3
            if k > 0:
                bb = pop(b, k)
                x, y = 96 + 110, 760
                img.alpha_composite(pop(av, k), (96, y + bb.height - 96))
                img.alpha_composite(bb, (x, y))
            yield img
    elif kind == "chat":
        msgs = sc["messages"]
        av_small = avatar(sc["who"], 76, sc.get("color", VIOLET))
        header = Image.new("RGBA", (W, 300), (255, 255, 255, 255))
        hd = ImageDraw.Draw(header)
        header.alpha_composite(avatar(sc["who"], 120, sc.get("color", VIOLET)), ((W - 120) // 2, 40))
        fn = render.font(48, 800)
        hd.text(((W - fn.getlength(sc["who"])) / 2, 172), sc["who"], font=fn, fill=INK)
        fr = render.font(34, 600)
        hd.text(((W - fr.getlength(sc.get("role", ""))) / 2, 232), sc.get("role", ""), font=fr, fill=MUTED)
        hd.line([(0, 299), (W, 299)], fill=LINE, width=2)
        images = []
        for m in msgs:
            if "photo" in m:
                src = m["photo"]
                if isinstance(src, dict):  # one frame out of a clip
                    d, fr = clip_frames(src, 1)
                    tmp_dirs.append(d)
                    src = str(fr[0])
                ph = Image.open(Path(src).expanduser()) if isinstance(src, str) else src
                images.append(bubble(None, m["from"] == "me", photo=ph))
            else:
                images.append(bubble(m["text"], m["from"] == "me"))
        for i in range(n):
            t = i / FPS
            img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
            img.alpha_composite(header, (0, 150))
            y = 520
            for m, b in zip(msgs, images):
                if t < m["at"] - m.get("typing", 0):
                    break
                mine = m["from"] == "me"
                if t < m["at"]:  # the other side is typing
                    tb = typing_bubble(t)
                    img.alpha_composite(av_small, (70, y + tb.height - 76))
                    img.alpha_composite(tb, (166, y))
                    y += tb.height + 26
                    break
                bb = pop(b, (t - m["at"]) / 0.25)
                x = W - 70 - b.width if mine else 166
                if not mine:
                    img.alpha_composite(av_small, (70, y + b.height - 76))
                img.alpha_composite(bb, (x + (b.width - bb.width) // 2, y + (b.height - bb.height)))
                y += b.height + 26
                if m.get("react"):
                    em = emoji_image(m["react"], 64)
                    img.alpha_composite(em, (x + b.width - 50, y - 70))
            yield img
    elif kind == "headline":
        f = render.font(sc.get("size", 132), 800)
        ph = phone_image(sc["phone"], sc.get("phone_height", 1000)) if sc.get("phone") else None
        for i in range(n):
            t = i / FPS
            img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
            d = ImageDraw.Draw(img)
            y = 330
            for line in render.wrap(sc["text"], f, W - 2 * 90):
                words = " ".join("".join(p for p, _ in w) for w in line)
                d.text(((W - f.getlength(words)) / 2, y), words, font=f, fill=INK)
                y += round(f.size * 1.08)
            if sc.get("sub"):
                fs = render.font(50, 600)
                for line in render.wrap(sc["sub"], fs, W - 2 * 120):
                    words = " ".join("".join(p for p, _ in w) for w in line)
                    d.text(((W - fs.getlength(words)) / 2, y + 24), words, font=fs, fill=MUTED)
                    y += round(fs.size * 1.3)
            if ph is not None:
                e = 1 - (1 - min(1, t / 0.5)) ** 3
                py = round(H - ph.height * 0.78 + (1 - e) * 500)
                sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                ImageDraw.Draw(sh).rounded_rectangle([(W - ph.width) // 2 + 20, py + 30, (W + ph.width) // 2, py + ph.height], radius=90, fill=(30, 20, 60, 70))
                img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
                img.alpha_composite(ph, ((W - ph.width) // 2, py))
            yield img
    elif kind == "end":
        wm = wordmark(130)
        for i in range(n):
            t = i / FPS
            img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
            k = min(1, t / 0.35)
            img.alpha_composite(pop(wm, k), ((W - wm.width) // 2, 700))
            d = ImageDraw.Draw(img)
            fl = render.font(60, 700)
            if t > 0.3:
                d.text(((W - fl.getlength(sc["line"])) / 2, 900), sc["line"], font=fl, fill=INK)
            if t > 0.6:
                fc = render.font(46, 800)
                w = fc.getlength(sc["cta"]) + 100
                d.rounded_rectangle([(W - w) / 2, 1010, (W + w) / 2, 1110], radius=50, fill=VIOLET)
                d.text(((W - fc.getlength(sc["cta"])) / 2, 1033), sc["cta"], font=fc, fill=WHITE)
            yield img


def render_story(story, out):
    frames_dir = Path(tempfile.mkdtemp())
    tmp_dirs = [frames_dir]
    n = 0
    try:
        for sc in story["scenes"]:
            for img in scene_frames(sc, tmp_dirs):
                n += 1
                img.convert("RGB").save(frames_dir / f"{n:05d}.png", compress_level=1)
        subprocess.run([str(render.encoder()), str(frames_dir), str(FPS), str(out)], check=True, stdout=subprocess.DEVNULL)
    finally:
        for d in tmp_dirs:
            shutil.rmtree(d, ignore_errors=True)
    return n / FPS


if __name__ == "__main__":
    spec = runpy.run_path(sys.argv[1])
    story = spec["STORIES"][sys.argv[2]]
    print(render_story(story, sys.argv[3] if len(sys.argv) > 3 else f"/tmp/{sys.argv[2]}.mp4"))


def sound_events(story):
    """Where the phone sounds go: a pop for each message that arrives, keys while you type and a
    soft send for each of yours, a whoosh on the headline, a chime on the mark."""
    events, start = [], 0.0
    for sc in story["scenes"]:
        if sc["kind"] == "photo":
            events.append((start + 0.25, "receive", 0.9, None, 0.0))
        elif sc["kind"] == "chat":
            for i, m in enumerate(sc["messages"]):
                at = start + m["at"]
                if m["from"] == "me":
                    events.append((max(start, at - 0.95), "typing", 0.55, 0.85, 1.5 + 2.1 * i))
                    events.append((at, "send", 0.8, None, 0.0))
                elif m["at"] > 0:
                    events.append((at, "receive", 0.9, None, 0.0))
        elif sc["kind"] == "headline":
            events.append((start + 0.05, "whoosh", 0.7, None, 0.0))
        elif sc["kind"] == "end":
            events.append((start + 0.15, "chime", 0.6, None, 0.0))
        start += sc["secs"]
    return events
