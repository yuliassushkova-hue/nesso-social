"""Seamless carousels: one long picture cut into 4:5 slides, so a sentence that starts on one slide
ends on the next and a phone stands across the cut. The swipe is what finishes the thought.

    from panorama import render_panorama
    render_panorama(spec, out_dir)   # writes 01.jpg, 02.jpg, ...

spec = {
  "slides": 7,
  "photos": [{"file", "x", "focus": 0..1 (horizontal crop centre, optional)}],   # left to right
  "blocks": [{"x", "y", "lines": [("text", "white"|"violet"|"orange"|"ink", size)]}],
  "phones": [{"mock", "x" (centre), "y" (top), "height", "tilt"}],
  "mark": {"x" (centre), "y", "height", "word": "white"|"ink", "sub"},
  "hint": True,
}
Photos are blended into each other over `feather` pixels, so no cut shows between them.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

import render

SW, SH = 1080, 1350
STYLES = {"white": (render.WHITE, render.INK), "violet": (render.VIOLET, render.WHITE),
          "orange": (render.ORANGE, render.WHITE), "ink": (render.INK, render.WHITE)}


def _photo_layer(path, height, width=None, focus=0.5):
    im = Image.open(Path(path).expanduser()).convert("RGB")
    scale = height / im.height
    im = im.resize((round(im.width * scale), height), Image.LANCZOS)
    if width and im.width > width:
        left = round((im.width - width) * focus)
        im = im.crop((left, 0, left + width, height))
    return im


def render_panorama(spec, out_dir, feather=320):
    n = spec["slides"]
    W = SW * n
    canvas = Image.new("RGBA", (W, SH), render.WHITE + (255,))
    photos = spec["photos"]
    for i, p in enumerate(photos):
        nxt = photos[i + 1]["x"] if i + 1 < len(photos) else W
        width = (nxt - p["x"]) + (feather if i + 1 < len(photos) else 0)
        im = _photo_layer(p["file"], SH, width, p.get("focus", 0.5)).convert("RGBA")
        mask = Image.new("L", im.size, 255)
        md = ImageDraw.Draw(mask)
        if i > 0:  # fade in from the photo before
            for x in range(feather):
                md.line([(x, 0), (x, SH)], fill=round(255 * x / feather))
        canvas.alpha_composite(Image.composite(im, Image.new("RGBA", im.size, (0, 0, 0, 0)), mask), (p["x"], 0))
    d = ImageDraw.Draw(canvas)
    for ph in spec.get("phones", []):
        phone = render.phone_crop(ph["mock"])
        h = ph["height"]
        phone = phone.resize((round(phone.width * h / phone.height), h), Image.LANCZOS)
        tilted = phone.rotate(ph.get("tilt", -4), resample=Image.BICUBIC, expand=True)
        x0, y0 = ph["x"] - tilted.width // 2, ph["y"]
        shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle([x0 + 40, y0 + 50, x0 + tilted.width + 10, y0 + tilted.height + 10], radius=100, fill=(20, 10, 40, 140))
        canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(40)))
        canvas.alpha_composite(tilted, (x0, y0))
    for blk in spec.get("blocks", []):
        y = blk["y"]
        for text, style, size in blk["lines"]:
            f = render.font(size, 800)
            fill, fg = STYLES[style]
            pad_x, pad_y = round(size * 0.3), round(size * 0.16)
            top_, bottom_ = f.getbbox("Hg")[1], f.getbbox("Hg")[3]
            h = bottom_ - top_
            w = f.getlength(text)
            x = blk["x"]
            d.rounded_rectangle([x, y, x + w + 2 * pad_x, y + h + 2 * pad_y], radius=round(size * 0.2), fill=fill)
            d.text((x + pad_x, y + pad_y - top_), text, font=f, fill=fg)
            y += h + 2 * pad_y + 12
    if spec.get("mark"):
        m = spec["mark"]
        wm = render.wordmark(m.get("height", 120), render.WHITE if m.get("word", "white") == "white" else render.INK)
        box_w, box_h = wm.width + 120, wm.height + (110 if m.get("sub") else 60)
        bx, by = m["x"] - box_w // 2, m["y"]
        d.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=50, fill=(255, 255, 255, 235) if m.get("word") == "ink" else (22, 24, 28, 200))
        canvas.alpha_composite(wm, (m["x"] - wm.width // 2, by + 30))
        if m.get("sub"):
            fs = render.font(44, 800)
            col = render.INK if m.get("word") == "ink" else render.WHITE
            d.text((m["x"] - fs.getlength(m["sub"]) / 2, by + wm.height + 40), m["sub"], font=fs, fill=col)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    names = []
    for i in range(n):
        sl = canvas.crop((i * SW, 0, (i + 1) * SW, SH)).convert("RGB")
        if i == 0 and spec.get("hint", True):
            dd = ImageDraw.Draw(sl)
            fh = render.font(40, 800)
            hint = "Scorri  →"
            bw = fh.getlength(hint) + 70
            dd.rounded_rectangle([SW - 96 - bw, SH - 140, SW - 96, SH - 60], radius=40, fill=render.WHITE)
            dd.text((SW - 96 - bw + 35, SH - 125), hint, font=fh, fill=render.INK)
        name = f"{i + 1:02d}.jpg"
        sl.save(out / name, "JPEG", quality=92)
        names.append(name)
    return names
