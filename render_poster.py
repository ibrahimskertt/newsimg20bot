#!/usr/bin/env python3
"""
render_poster.py - Generates entry.png for the news-image-20261120 competition.
Poster dimensions: 1024x1024 pixels, strictly <= 1 MiB.
Summarizes the world news of Friday, November 20, 2026.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_poster():
    width, height = 1024, 1024
    img = Image.new("RGB", (width, height), color="#0B1220")
    draw = ImageDraw.Draw(img)

    # 1. Background gradient (Deep ink navy #0B1220 to #12233F)
    for y in range(height):
        r = int(11 + (18 - 11) * (y / height))
        g = int(18 + (35 - 18) * (y / height))
        b = int(32 + (63 - 32) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Font paths
    font_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_reg_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    try:
        f_kicker = ImageFont.truetype(font_bold_path, 13)
        f_date = ImageFont.truetype(font_bold_path, 32)
        f_hero_title = ImageFont.truetype(font_bold_path, 25)
        f_hero_sub = ImageFont.truetype(font_reg_path, 14)
        f_hero_note = ImageFont.truetype(font_bold_path, 13)
        f_chip_tag = ImageFont.truetype(font_bold_path, 12)
        f_chip_title = ImageFont.truetype(font_bold_path, 14)
        f_chip_body = ImageFont.truetype(font_reg_path, 12)
        f_footer = ImageFont.truetype(font_reg_path, 11)
        f_section_title = ImageFont.truetype(font_bold_path, 16)
        f_section_sub = ImageFont.truetype(font_reg_path, 13)
    except IOError:
        f_kicker = f_date = f_hero_title = f_hero_sub = f_hero_note = f_chip_tag = f_chip_title = f_chip_body = f_footer = f_section_title = f_section_sub = ImageFont.load_default()

    # Colors
    c_gold = "#D4AF37"
    c_white = "#F7F3E9"
    c_muted = "#C9D6F2"
    c_ivory = "#F4EDDE"
    c_ink = "#14213D"
    c_red = "#C0392B"
    c_chip_bg = "#162747"

    # --- 1. MASTHEAD ---
    draw.text((40, 28), "T H E   W O R L D   I N   O N E   I M A G E", fill=c_gold, font=f_kicker)
    draw.text((40, 50), "FRIDAY, NOVEMBER 20, 2026", fill=c_white, font=f_date)
    draw.line([(40, 92), (984, 92)], fill=c_gold, width=2)

    # --- 2. HERO PANEL (Kyiv Attack Graphic) ---
    panel_x1, panel_y1, panel_x2, panel_y2 = 40, 105, 984, 315
    draw.rounded_rectangle([panel_x1, panel_y1, panel_x2, panel_y2], radius=12, fill="#080E1A", outline=c_gold, width=1)

    # City skyline silhouette
    skyline_y = panel_y2 - 38
    buildings = [
        (60, skyline_y - 28, 90, panel_y2),
        (95, skyline_y - 48, 140, panel_y2),
        (145, skyline_y - 24, 175, panel_y2),
        (180, skyline_y - 62, 230, panel_y2),
        (235, skyline_y - 38, 280, panel_y2),
        (320, skyline_y - 42, 370, panel_y2),
        (375, skyline_y - 70, 430, panel_y2),
        (435, skyline_y - 34, 475, panel_y2),
        (550, skyline_y - 48, 600, panel_y2),
        (605, skyline_y - 28, 645, panel_y2),
        (680, skyline_y - 58, 740, panel_y2),
        (745, skyline_y - 38, 790, panel_y2),
        (850, skyline_y - 52, 910, panel_y2),
        (915, skyline_y - 28, 960, panel_y2),
    ]
    for b_box in buildings:
        draw.rectangle(b_box, fill="#111B30")

    # River (Dnipro river) across lower part
    river_y1 = panel_y2 - 56
    river_y2 = panel_y2 - 20
    draw.rectangle([panel_x1 + 1, river_y1, panel_x2 - 1, river_y2], fill="#1B2B48")

    # Three bridges spanning the river with one broken
    bridge_xs = [250, 512, 774]
    for i, bx in enumerate(bridge_xs):
        draw.arc([bx - 55, river_y1 - 10, bx + 55, river_y2 + 4], start=180, end=360, fill="#8A9BB8", width=3)
        draw.line([(bx - 60, river_y1), (bx + 60, river_y1)], fill="#C9D6F2", width=2)
        if i == 1: # damaged bridge
            draw.line([(bx - 12, river_y1), (bx + 12, river_y1)], fill="#080E1A", width=4)
            draw.ellipse([bx - 14, river_y1 - 10, bx + 14, river_y1 + 6], fill=c_red)
            draw.ellipse([bx - 7, river_y1 - 6, bx + 7, river_y1 + 2], fill="#F39C12")

    # Missile trails and drones
    draw.line([(200, panel_y1 + 15), (320, skyline_y - 18)], fill=c_red, width=2)
    draw.ellipse([317, skyline_y - 21, 323, skyline_y - 15], fill="#FFFFFF")
    
    draw.line([(450, panel_y1 + 10), (510, skyline_y - 28)], fill=c_red, width=2)
    draw.ellipse([507, skyline_y - 31, 513, skyline_y - 25], fill="#FFFFFF")
    
    draw.line([(700, panel_y1 + 18), (780, skyline_y - 22)], fill="#F39C12", width=2)
    draw.ellipse([777, skyline_y - 25, 783, skyline_y - 19], fill="#FFFFFF")

    drone_dots = [(150, 125), (280, 115), (390, 132), (580, 120), (650, 128), (820, 118), (900, 138)]
    for dx, dy in drone_dots:
        draw.ellipse([dx-2, dy-2, dx+2, dy+2], fill=c_gold)

    # Panel label
    draw.rectangle([panel_x1 + 12, panel_y1 + 12, panel_x1 + 175, panel_y1 + 32], fill="#162747")
    draw.text((panel_x1 + 18, panel_y1 + 15), "KYIV OVERNIGHT ASSAULT", fill=c_gold, font=f_kicker)


    # --- 3. HERO HEADLINE & SUBLINE ---
    y_cursor = 330
    draw.text((40, y_cursor), "RUSSIA'S BIGGEST AIR ASSAULT OF THE WAR", fill=c_white, font=f_hero_title)
    
    y_cursor += 33
    sub_text = "110+ missiles, 400+ drones rain on Ukraine overnight — 8 killed, Kyiv's bridges hit, power cut — hours after Trump–Putin talks."
    draw.text((40, y_cursor), sub_text, fill=c_muted, font=f_hero_sub)

    y_cursor += 22
    draw.text((40, y_cursor), "⚠  Two missiles and a drone strayed into Polish airspace during the bombardment", fill=c_gold, font=f_hero_note)


    # --- 4. SECOND-STORY BAND (UK AND EU STRIKE NEW DEAL) ---
    band_y1, band_y2 = 410, 530
    draw.rounded_rectangle([40, band_y1, 984, band_y2], radius=10, fill=c_ivory)

    icon_cx, icon_cy = 95, (band_y1 + band_y2) // 2
    # Circle radius 32 (diameter 64) for EU·UK badge so text sits fully inside with clear padding
    draw.ellipse([icon_cx - 32, icon_cy - 32, icon_cx + 32, icon_cy + 32], fill=c_ink)
    draw.text((icon_cx - 18, icon_cy - 9), "EU·UK", fill=c_gold, font=f_kicker)

    draw.text((155, band_y1 + 18), "UK AND EU STRIKE NEW DEAL", fill=c_ink, font=f_section_title)
    
    deal_desc = "Food exports, youth mobility and carbon emissions agreed at second EU-UK summit in Brussels.\nPrime Minister Andy Burnham: Britain will explore even closer ties."
    draw.text((155, band_y1 + 46), deal_desc, fill="#333333", font=f_section_sub)


    # --- 5. BOTTOM ROW OF THREE CHIPS ---
    chip_y1, chip_y2 = 555, 765
    chip_width = 300
    chip_gap = 42
    left_margin = 40

    chips_data = [
        {
            "tag": "AI ABROAD",
            "title": "US Threatens AI Ban",
            "body": "Trump threatens a ban on US firms building AI data centres overseas, providing little detail on the potential policy."
        },
        {
            "tag": "TECH SLIDE",
            "title": "Anthropic Shares Fall",
            "body": "Shares in Anthropic fall a day after record $81B IPO as a wider tech sell-off continues across markets."
        },
        {
            "tag": "MERCURY",
            "title": "BepiColombo Arrives",
            "body": "BepiColombo spacecraft arrives at Mercury after an eight-year journey through space."
        }
    ]

    for i, chip in enumerate(chips_data):
        cx1 = left_margin + i * (chip_width + chip_gap)
        cx2 = cx1 + chip_width
        draw.rounded_rectangle([cx1, chip_y1, cx2, chip_y2], radius=10, fill=c_chip_bg, outline="#1E335E", width=1)
        
        # Tag pill
        draw.rectangle([cx1 + 16, chip_y1 + 16, cx1 + 105, chip_y1 + 36], fill="#0B1220")
        draw.text((cx1 + 22, chip_y1 + 19), chip["tag"], fill=c_gold, font=f_chip_tag)

        # Title
        draw.text((cx1 + 16, chip_y1 + 48), chip["title"], fill=c_white, font=f_chip_title)

        # Body text wrapping
        words = chip["body"].split()
        lines = []
        cur_line = []
        for w in words:
            cur_line.append(w)
            test_line = " ".join(cur_line)
            if len(test_line) > 36:
                cur_line.pop()
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))

        by = chip_y1 + 80
        for line in lines[:4]:
            draw.text((cx1 + 16, by), line, fill=c_muted, font=f_chip_body)
            by += 20


    # --- 6. ADDITIONAL WORLD NEWS / BRIEFINGS ---
    brief_y1, brief_y2 = 790, 930
    draw.rounded_rectangle([40, brief_y1, 984, brief_y2], radius=10, fill="#121D33", outline="#1E335E", width=1)
    
    draw.text((65, brief_y1 + 16), "AROUND THE WORLD ON FRIDAY, 20 NOVEMBER 2026", fill=c_gold, font=f_kicker)

    briefs = [
        "• Iran: Explosion and smoke on Qeshm Island caused by the disposal of unexploded munitions (Tasnim / Reuters).",
        "• United States: Indian man sentenced to more than 19 years in prison over plot to assassinate Sikh separatist leader.",
        "• Europe: Cost-of-living protests sweep across Europe."
    ]
    by = brief_y1 + 42
    for b in briefs:
        draw.text((65, by), b, fill=c_white, font=f_section_sub)
        by += 28


    # --- 7. FOOTER LINE ---
    footer_y = 955
    draw.line([(40, footer_y), (984, footer_y)], fill="#1E335E", width=1)
    footer_text = "Also Friday: blast on Iran's Qeshm Island · Indian man jailed 19 years over Sikh assassination plot · cost-of-living protests sweep Europe — Sources: Reuters · BBC · AP"
    draw.text((40, footer_y + 16), footer_text, fill="#8A9BB8", font=f_footer)

    # Save output
    output_path = "entry.png"
    img.save(output_path, "PNG")
    print(f"Poster successfully generated: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    create_poster()
