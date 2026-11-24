#!/usr/bin/env python3
"""Draw a one-page newspaper front page summing up the world news of
Monday 23 November 2026, and save it as entry.png (1024x1024).

Everything is drawn with Pillow primitives: no photos, no network,
fully deterministic output.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (18, 18, 22)
NAVY = (16, 42, 92)
RED = (168, 28, 32)
GREEN = (18, 110, 56)
GOLD = (176, 124, 22)
GREY = (92, 92, 96)
PANEL = (255, 253, 246)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, text, fnt, fill, max_w, leading=1.25):
    lines = wrap(draw, text, fnt, max_w)
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def panel(draw, box, kicker, kicker_fill, headline, caption, head_size=30,
          text_w=None, caption_size=19):
    """A story panel: border, kicker label, headline, caption.
    text_w optionally narrows the text column (leaving room for an icon)."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=10, fill=PANEL, outline=INK, width=2)
    pad = 16
    tw = text_w if text_w is not None else (x1 - x0 - 2 * pad)
    draw.text((x0 + pad, y0 + 10), kicker, font=font(SANS_B, 17), fill=kicker_fill)
    hy = y0 + 38
    hy = draw_text_block(draw, x0 + pad, hy, headline, font(SERIF_B, head_size),
                         INK, tw, leading=1.12)
    draw.line([(x0 + pad, hy + 2), (x0 + pad + tw, hy + 2)], fill=GREY, width=1)
    draw_text_block(draw, x0 + pad, hy + 10, caption, font(SANS, caption_size),
                    (40, 40, 44), tw, leading=1.3)
    return hy


def masthead(draw):
    draw.rectangle([0, 0, W, H], fill=PAPER)
    draw.rectangle([14, 14, W - 14, H - 14], outline=INK, width=3)
    draw.rectangle([22, 22, W - 22, H - 22], outline=INK, width=1)
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_B, 58)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 30), title, font=tf, fill=INK)
    draw.line([(40, 108), (W - 40, 108)], fill=INK, width=3)
    date = "Monday 23 November 2026"
    df = font(SERIF_B, 33)
    dw = draw.textlength(date, font=df)
    draw.text(((W - dw) / 2, 118), date, font=df, fill=RED)
    sub = "The whole day's world news on a single page - six stories, five continents"
    sf = font(SANS, 18)
    sw = draw.textlength(sub, font=sf)
    draw.text(((W - sw) / 2, 160), sub, font=sf, fill=GREY)
    draw.line([(40, 190), (W - 40, 190)], fill=INK, width=2)


def chip_icon(draw, cx, cy, s):
    """A computer chip with pins and a rising chart arrow over it."""
    draw.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=14,
                           fill=NAVY, outline=INK, width=3)
    inner = int(s * 0.55)
    draw.rounded_rectangle([cx - inner, cy - inner, cx + inner, cy + inner],
                           radius=8, outline=(220, 226, 240), width=3)
    for i in range(-2, 3):
        off = i * int(s * 0.36)
        draw.line([(cx + off, cy - s - 16), (cx + off, cy - s)], fill=INK, width=5)
        draw.line([(cx + off, cy + s), (cx + off, cy + s + 16)], fill=INK, width=5)
        draw.line([(cx - s - 16, cy + off), (cx - s, cy + off)], fill=INK, width=5)
        draw.line([(cx + s, cy + off), (cx + s + 16, cy + off)], fill=INK, width=5)
    pts = [(cx - inner, cy + int(inner * 0.6)), (cx - int(inner * 0.3), cy),
           (cx + int(inner * 0.15), cy + int(inner * 0.25)),
           (cx + inner, cy - int(inner * 0.7))]
    draw.line(pts, fill=(64, 220, 120), width=6, joint="curve")
    ax, ay = pts[-1]
    draw.polygon([(ax, ay), (ax - 18, ay + 2), (ax - 4, ay + 16)], fill=(64, 220, 120))


def lead_story(draw):
    box = (40, 202, 984, 462)
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=10, fill=PANEL, outline=INK, width=2)
    pad = 18
    draw.text((x0 + pad, y0 + 12), "BUSINESS  •  UNITED STATES",
              font=font(SANS_B, 18), fill=NAVY)
    hy = draw_text_block(
        draw, x0 + pad, y0 + 42,
        "NVIDIA BRINGS BACK HUANG - AND WALL STREET ERUPTS",
        font(SERIF_B, 36), INK, 600, leading=1.12)
    draw_text_block(
        draw, x0 + pad, hy + 10,
        "Jensen Huang returns as chief executive 11 days after resigning. "
        "Nvidia shares leap about 31%; the Nasdaq jumps 6.5% and the "
        "S&P 500 climbs 4.7%.",
        font(SANS, 20), (40, 40, 44), 600, leading=1.3)
    chip_icon(draw, 800, 326, 74)
    draw.text((724, 428), "CHIP GIANT", font=font(SANS_B, 15), fill=GREY)


def ship_icon(draw, cx, cy, s):
    """A warship on waves."""
    draw.polygon([(cx - s, cy), (cx + s, cy), (cx + int(s * 0.7), cy + int(s * 0.45)),
                  (cx - int(s * 0.7), cy + int(s * 0.45))], fill=NAVY, outline=INK)
    draw.rectangle([cx - int(s * 0.45), cy - int(s * 0.35), cx + int(s * 0.2), cy],
                   fill=NAVY, outline=INK)
    draw.line([(cx + int(s * 0.35), cy - int(s * 0.8)), (cx + int(s * 0.35), cy)],
              fill=INK, width=3)
    for dx in (-0.6, 0.0, 0.6):
        x = cx + int(dx * s)
        draw.arc([x - 16, cy + int(s * 0.5), x + 16, cy + int(s * 0.95)],
                 start=0, end=180, fill=(40, 100, 170), width=3)


def tanker_icon(draw, cx, cy, s):
    """An oil tanker with a flame above its deck."""
    draw.polygon([(cx - s, cy + 10), (cx + s, cy + 10), (cx + int(s * 0.75), cy + int(s * 0.5)),
                  (cx - int(s * 0.75), cy + int(s * 0.5))], fill=(120, 60, 20), outline=INK)
    draw.rectangle([cx - int(s * 0.8), cy - 4, cx + int(s * 0.55), cy + 10],
                   fill=(160, 84, 30), outline=INK)
    draw.rectangle([cx + int(s * 0.6), cy - int(s * 0.35), cx + int(s * 0.85), cy + 10],
                   fill=(90, 90, 96), outline=INK)
    fx, fy = cx - int(s * 0.2), cy - int(s * 0.55)
    draw.polygon([(fx, fy - 22), (fx + 11, fy + 4), (fx + 3, fy + 14),
                  (fx - 8, fy + 12), (fx - 12, fy)], fill=RED)
    draw.polygon([(fx, fy - 8), (fx + 6, fy + 6), (fx - 5, fy + 8)], fill=GOLD)


def globe_icon(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    draw.ellipse([cx - int(r * 0.45), cy - r, cx + int(r * 0.45), cy + r],
                 outline=NAVY, width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=NAVY, width=2)
    draw.line([(cx - int(r * 0.4), cy + int(r * 1.05)), (cx + int(r * 0.4), cy + int(r * 1.05))],
              fill=INK, width=3)


def train_icon(draw, cx, cy, s):
    draw.rounded_rectangle([cx - s, cy - int(s * 0.7), cx + s, cy + int(s * 0.35)],
                           radius=8, fill=GREEN, outline=INK, width=2)
    draw.rectangle([cx - int(s * 0.8), cy - int(s * 0.5), cx - int(s * 0.35), cy - int(s * 0.1)],
                   fill=(230, 240, 255), outline=INK)
    draw.rectangle([cx - int(s * 0.2), cy - int(s * 0.5), cx + int(s * 0.25), cy - int(s * 0.1)],
                   fill=(230, 240, 255), outline=INK)
    draw.ellipse([cx - int(s * 0.65), cy + int(s * 0.3), cx - int(s * 0.35), cy + int(s * 0.6)],
                 fill=INK)
    draw.ellipse([cx + int(s * 0.35), cy + int(s * 0.3), cx + int(s * 0.65), cy + int(s * 0.6)],
                 fill=INK)
    draw.line([(cx - s - 6, cy + int(s * 0.75)), (cx + s + 6, cy + int(s * 0.75))],
              fill=INK, width=3)


def shield_icon(draw, cx, cy, s):
    draw.polygon([(cx, cy - s), (cx + s, cy - int(s * 0.6)), (cx + s, cy + int(s * 0.3)),
                  (cx, cy + s), (cx - s, cy + int(s * 0.3)), (cx - s, cy - int(s * 0.6))],
                 fill=GOLD, outline=INK, width=2)
    star = []
    import math
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = s * 0.55 if i % 2 == 0 else s * 0.24
        star.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(star, fill=(255, 250, 230), outline=INK)


def mid_stories(draw):
    panel(draw, (40, 474, 502, 730), "WAR  •  LIBYA / UKRAINE", RED,
          "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
          "Zelenskyy says seven naval drones sank the Russian corvette "
          "Merkury in Benghazi port - the war spills far beyond Europe.",
          head_size=25, text_w=336)
    ship_icon(draw, 440, 590, 36)
    panel(draw, (522, 474, 984, 730), "MIDDLE EAST  •  IRAN", GOLD,
          "IRAN VOWS TO FIGHT US BLOCKADE",
          "Tehran says it will use all its tools against the US naval "
          "blockade, as Washington hits Iran's shadow-banking network; "
          "blasts rock the Strait of Hormuz.",
          head_size=25, text_w=336)
    tanker_icon(draw, 922, 588, 36)


def bottom_stories(draw):
    panel(draw, (40, 742, 341, 996), "CLIMATE  •  TÜRKIYE", GREEN,
          "COP31 ENDS WITH NO CLIMATE DEAL",
          "The UN climate summit in Türkiye ends without a new deal, "
          "deadlocked over fossil fuels and money. Pacific nations "
          "voice despair.",
          head_size=23, caption_size=17)
    globe_icon(draw, 298, 950, 19)
    panel(draw, (361, 742, 662, 996), "ASIA  •  NEPAL & INDIA", NAVY,
          "NEPAL AND INDIA SIGN EIGHT PACTS",
          "PM Balendra Shah ends his Delhi visit: eight pacts signed, "
          "the Ayodhya-Janakpur express launched, and a $1.6bn rebuild "
          "fund pledged by India.",
          head_size=23, caption_size=17)
    train_icon(draw, 612, 944, 24)
    panel(draw, (682, 742, 984, 996), "AMERICAS  •  MEXICO", RED,
          "'EL CHAPO ISIDRO' CAPTURED IN MEXICO",
          "Mexican special forces capture the Sinaloa cartel boss, an "
          "FBI most-wanted fugitive, with US intelligence help.",
          head_size=23, caption_size=17)
    shield_icon(draw, 936, 950, 19)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    lead_story(draw)
    mid_stories(draw)
    bottom_stories(draw)
    img.save("entry.png")
    print("saved entry.png")


if __name__ == "__main__":
    main()
