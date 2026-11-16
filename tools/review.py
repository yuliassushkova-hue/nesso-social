"""A "Casa da serie" carousel: a home from a film or a series, read the way a viewing would be.

Slide 1 is the still, full bleed, with the title. The middle slides put the still on top and a
cream panel underneath with a heading and two or three lines. The last slide asks the reader a
question and closes on the Nesso lockup. Stills are the series' own frames or free photos of the
real building; the credit line goes on the slide that shows them.

    {"review": {"label": "CASA DA SERIE", "title": "...", "show": "...",
                "cover": path, "cover_credit": "...",
                "slides": [{"photo": path, "focus": 0.5, "head": "...", "lines": [...], "credit": "..."}],
                "ask": "...", "ask_sub": "...", "cta": "Prova Nesso  →", "cta_sub": "link in bio"}}
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

import render
from render import CREAM, INK, ORANGE, VIOLET, WHITE, W, font, wordmark, wrap

SH = 1350
PAD = 84
SOFT = (110, 102, 98)


def cover(path, w, h, focus=0.5):
    """The photo scaled to fill w x h, cropped around a horizontal focus point."""
    im = Image.open(Path(path).expanduser()).convert("RGB")
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round(max(0, min(im.width - w, im.width * focus - w / 2)))
    y = round((im.height - h) / 2)
    return im.crop((x, y, x + w, y + h))


def text(d, x, y, words, f, fill, width):
    for line in wrap(words.replace("*", ""), f, width):
        d.text((x, y), " ".join("".join(p for p, _ in w) for w in line), font=f, fill=fill)
        y += round(f.size * 1.18)
    return y


def chip(d, x, y, words, fill, fg, size=34):
    f = font(size, 800)
    w = f.getlength(words)
    d.rounded_rectangle([x, y, x + w + 2 * 22, y + size + 2 * 14], radius=(size + 28) // 2, fill=fill)
    d.text((x + 22, y + 14 - f.getbbox("H")[1] + 4), words, font=f, fill=fg)
    return y + size + 28


def credit(img, words):
    if not words:
        return
    d = ImageDraw.Draw(img)
    f = font(22, 600)
    w = f.getlength(words)
    d.rounded_rectangle([W - PAD - w - 20, 30, W - PAD + 4, 30 + 38], radius=12, fill=(0, 0, 0, 120))
    d.text((W - PAD - w - 8, 38), words, font=f, fill=WHITE)


def counter(d, i, n, fill):
    f = font(30, 800)
    s = f"{i}/{n}"
    d.text((PAD, 44), s, font=f, fill=fill)


def first(spec, n):
    img = cover(spec["cover"], W, SH, spec.get("cover_focus", 0.5)).convert("RGBA")
    shade = Image.new("RGBA", (W, SH), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    for y in range(SH // 3, SH):
        a = round(230 * ((y - SH // 3) / (SH * 2 / 3)) ** 1.4)
        sd.line([(0, y), (W, y)], fill=(18, 14, 30, a))
    img.alpha_composite(shade)
    d = ImageDraw.Draw(img)
    counter(d, 1, n, WHITE)
    credit(img, spec.get("cover_credit"))
    f_title, f_show = font(104, 800), font(44, 700)
    lines = wrap(spec["title"], f_title, W - 2 * PAD)
    y = SH - 120 - len(lines) * round(104 * 1.06) - 60 - 60
    y = chip(d, PAD, y, spec.get("label", "CASA DA SERIE"), ORANGE, WHITE) + 26
    for line in lines:
        d.text((PAD, y), " ".join("".join(p for p, _ in w) for w in line), font=f_title, fill=WHITE)
        y += round(104 * 1.06)
    d.text((PAD, y + 18), spec["show"], font=f_show, fill=(235, 228, 255))
    d.text((W - PAD - font(36, 800).getlength("Scorri  →"), SH - 84), "Scorri  →", font=font(36, 800), fill=WHITE)
    return img.convert("RGB")


def middle(slide, i, n):
    top = 760
    img = Image.new("RGBA", (W, SH), CREAM + (255,))
    img.paste(cover(slide["photo"], W, top, slide.get("focus", 0.5)), (0, 0))
    credit(img, slide.get("credit"))
    d = ImageDraw.Draw(img)
    counter(d, i, n, WHITE)
    y = top + 56
    y = chip(d, PAD, y, slide["head"], slide.get("chip", VIOLET), WHITE, 36) + 30
    for line in slide["lines"]:
        f = font(46, 700)
        d.ellipse([PAD, y + 18, PAD + 16, y + 34], fill=ORANGE)
        y = text(d, PAD + 38, y, line, f, INK, W - 2 * PAD - 38) + 18
    return img.convert("RGB")


def last(spec, i, n):
    img = cover(spec["cover"], W, SH, spec.get("cover_focus", 0.5)).filter(ImageFilter.GaussianBlur(26)).convert("RGBA")
    img.alpha_composite(Image.new("RGBA", (W, SH), (32, 22, 70, 170)))
    d = ImageDraw.Draw(img)
    counter(d, i, n, WHITE)
    y = 300
    y = text(d, PAD, y, spec["ask"], font(96, 800), WHITE, W - 2 * PAD) + 20
    y = text(d, PAD, y, spec.get("ask_sub", "Scrivilo nei commenti 👇".replace(" 👇", "")), font(48, 600), (235, 228, 255), W - 2 * PAD) + 120
    y = text(d, PAD, y, spec.get("cta", "Prova Nesso  →"), font(84, 800), ORANGE, W - 2 * PAD)
    text(d, PAD, y + 4, spec.get("cta_sub", "link in bio"), font(52, 700), WHITE, W - 2 * PAD)
    mark = wordmark(130, WHITE)
    img.alpha_composite(mark, (W - PAD - mark.width, SH - 110 - mark.height))
    return img.convert("RGB")


def render_review(spec, folder):
    n = len(spec["slides"]) + 2
    pages = [first(spec, n)] + [middle(s, i + 2, n) for i, s in enumerate(spec["slides"])] + [last(spec, n, n)]
    names = []
    for i, page in enumerate(pages, 1):
        name = f"{i:02d}.jpg"
        page.save(folder / name, quality=92)
        names.append(name)
    return names
