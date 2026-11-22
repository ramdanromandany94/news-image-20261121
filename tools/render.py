#!/usr/bin/env python3
"""Render the 21 November 2026 world-news front page (1024x1024 PNG).

DRAFT: newspaper front page in the style of the 20 November entry —
masthead, date line, hero on the Kryvyi Rih double-tap, a 2x2 grid
(Mexico cartel boss / COP31 / markets & tech / Peru quake), a three-box
strip (Trump-Iran / Anthropic IPO / Gaza), an ALSO TODAY strip and a
sources footer. Deterministic: no timestamps, no randomness, no network.
Run: python3 tools/render.py writes entry.png next to this script's
parent directory.

REVISED: hero bursts moved down (ey 366–370) and shrunk so their rays
clear the second subline — the draft's middle burst sat behind "20" in
"2 killed — a boy, 7, and a paramedic, 20 — 60 wounded".
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "entry.png")

PAPER = (246, 241, 229)
INK = (17, 17, 17)
RED = (163, 22, 33)
NAVY = (27, 42, 74)
GREY = (90, 88, 80)
LIGHT = (255, 255, 255)
HERO_BG = (28, 30, 40)
ORANGE = (255, 150, 40)
YELLOW = (255, 210, 60)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, max_w, text, fnt, fill=INK, leading=1.25):
    lines = wrap(draw, text, fnt, max_w)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def rule(draw, x0, y, x1, wdt=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def burst(d, ex, ey, r):
    """Explosion starburst; kept low in the hero so it never covers text."""
    for k in range(8):
        a = math.pi * k / 4
        d.line([(ex, ey), (ex + int(r * 1.5 * math.cos(a)),
                           ey + int(r * 1.5 * math.sin(a)))],
               fill=ORANGE, width=5)
    d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=ORANGE)
    d.ellipse([ex - r // 2, ey - r // 2, ex + r // 2, ey + r // 2], fill=YELLOW)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- masthead ----
    d.rectangle([10, 10, W - 11, 96], fill=NAVY)
    d.text((512, 30), "THE WORLD IN ONE IMAGE", font=font(SERIF_B, 44),
           fill=LIGHT, anchor="ma")
    d.text((512, 74), "A NEWSPAPER OF SATURDAY'S NEWS  •  ONE PAGE, THE WHOLE WORLD",
           font=font(SANS, 15), fill=(200, 205, 220), anchor="ma")

    # ---- date line ----
    d.text((512, 108), "SATURDAY 21 NOVEMBER 2026", font=font(SERIF_B, 46),
           fill=RED, anchor="ma")
    rule(d, 60, 164, 964, 2)
    rule(d, 60, 168, 964, 1)

    # ---- hero: Kryvyi Rih double-tap ----
    hx0, hy0, hx1, hy1 = 24, 178, 1000, 440
    d.rectangle([hx0, hy0, hx1, hy1], fill=HERO_BG)
    # city skyline silhouette (low, below the text)
    d.rectangle([hx0, 384, hx1, hy1], fill=(52, 68, 96))
    for bx, bw, bh in ((60, 70, 60), (170, 50, 90), (260, 80, 45), (380, 55, 75),
                       (470, 75, 55), (580, 50, 95), (670, 85, 50), (790, 60, 80),
                       (880, 70, 55), (960, 40, 70)):
        d.rectangle([bx, 384 - bh, bx + bw, 384], fill=(40, 44, 58))
    # bursts sit between the buildings, clear of every text line
    burst(d, 330, 368, 20)
    burst(d, 640, 366, 24)
    burst(d, 930, 370, 18)
    d.text((512, 190), "KRYVYI RIH DOUBLE-TAP", font=font(SERIF_B, 52),
           fill=LIGHT, anchor="ma", stroke_width=2, stroke_fill=HERO_BG)
    d.text((512, 260), "Two ballistic missiles, then drones on the rescuers",
           font=font(SANS_B, 24), fill=LIGHT, anchor="ma")
    d.text((512, 292), "2 killed — a boy, 7, and a paramedic, 20 — 60 wounded",
           font=font(SANS_B, 24), fill=LIGHT, anchor="ma")
    d.text((512, 404), "Zelenskyy's home city  •  25 apartment blocks, a hospital, schools hit",
           font=font(SANS, 19), fill=(220, 225, 235), anchor="ma")

    # ---- 2x2 grid (rows tall enough for headline + 3 body lines) ----
    panels = [
        ("MEXICO CARTEL BOSS", RED, "'El Chapo Isidro' captured",
         "FBI top-10 fugitive Fausto Isidro Meza Flores seized in Guasave, "
         "Sinaloa, with US intel; gun battles kill 11."),
        ("COP31 ANTALYA", NAVY, "Climate talks in overtime",
         "No deal after two weeks in Antalya. The draft drops all mention of "
         "fossil fuels; a third text is due Saturday."),
        ("MARKETS & TECH", NAVY, "AI sell-off sinks stocks",
         "S&P 500 -3.7% on Friday, Nasdaq -5.3%, Nikkei -5.06%. Chip shares "
         "fall 10.7% as the AI rally unwinds."),
        ("PERU QUAKE", RED, "M6.7 quake shakes Peru",
         "Strong tremor in the Junin region, felt in Lima; residents rush into "
         "the streets. No deaths reported."),
    ]
    boxes = [(24, 452, 504, 608), (520, 452, 1000, 608),
             (24, 616, 504, 772), (520, 616, 1000, 772)]
    for (x0, y0, x1, y1), (kick, col, head, body) in zip(boxes, panels):
        d.rectangle([x0, y0, x1, y1], outline=INK, width=2)
        d.rectangle([x0, y0, x1, y0 + 28], fill=col)
        d.text((x0 + 12, y0 + 4), kick, font=font(SANS_B, 16), fill=LIGHT)
        y = para(d, x0 + 12, y0 + 36, x1 - x0 - 24, head,
                 font(SERIF_B, 25), leading=1.12)
        para(d, x0 + 12, y + 4, x1 - x0 - 24, body, font(SANS, 17), leading=1.28)

    # ---- Trump-Iran / Anthropic / Gaza strip (three boxes) ----
    sy0, sy1 = 784, 856
    strips = [
        (24, 341, "TRUMP–IRAN", RED,
         "Weighs new Iran strikes; decision after the New Year."),
        (353, 670, "ANTHROPIC IPO", NAVY,
         "Debut tops $2tn, then falls 8.5% on Friday."),
        (682, 999, "GAZA", RED,
         "4 killed as the ceasefire frays; 1,671 dead since the truce."),
    ]
    for x0, x1, kick, col, body in strips:
        d.rectangle([x0, sy0, x1, sy1], outline=INK, width=2)
        d.text((x0 + 12, sy0 + 6), kick, font=font(SANS_B, 16), fill=col)
        para(d, x0 + 12, sy0 + 30, x1 - x0 - 24, body,
             font(SANS, 15), leading=1.25)

    # ---- ALSO TODAY ----
    ay0 = 868
    d.text((512, ay0), "ALSO TODAY", font=font(SANS_B, 18), fill=INK, anchor="ma")
    rule(d, 380, ay0 + 26, 644, 1)
    also = ("BepiColombo reaches Mercury orbit after 8 years  •  Salvadoran troops fight "
            "gangs in Haiti  •  Haitian forces kill 34 suspected gang members  •  Russian "
            "cargo ship burns in the Baltic")
    para(d, 40, ay0 + 34, 944, also, font(SANS, 16), fill=GREY, leading=1.3)

    # ---- footer ----
    rule(d, 24, 986, 1000, 1)
    d.text((512, 992), "Sources: AP · Reuters · AFP · Euronews · OneTurn · ESA  •  make.fun/news-image-20261121",
           font=font(SANS, 13), fill=GREY, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
