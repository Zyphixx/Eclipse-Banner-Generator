from PIL import Image, ImageDraw, ImageFont


def create_banner(
    background_color,
    text_color,
    main_nick,
    main_nick_x,
    main_nick_y,
    sub_nick,
    sub_nick_x,
    sub_nick_y,
    description,
    description_x,
    description_y,
    twitter_username,
    twitter_username_x,
    twitter_username_y,
    character_path,
    character_x,
    character_y,
    logo1_path,
    logo1_x,
    logo1_y,
    logo1_width,
    logo1_height,
    logo2_path,
    logo2_x,
    logo2_y,
    logo2_width,
    logo2_height,
    output_path,
    line1_x,
    line1_x2,
    line1_y,  
    line1_color,
    line1_width,
    line2_x,
    line2_x2,
    line2_y,  
    line2_color,
    line2_width,
):

    banner = Image.new("RGB", (1500, 500), background_color)
    draw = ImageDraw.Draw(banner)


    main_nick_font = ImageFont.truetype("fonts/barlow.ttf", 140)
    sub_nick_font = ImageFont.truetype("fonts/alpina.otf", 140)
    description_font = ImageFont.truetype("fonts/atlas.otf", 27)
    twitter_font = ImageFont.truetype("fonts/atlas.otf", 27)
    special_font = ImageFont.truetype("fonts/MYRIADPRO-REGULAR.otf", 27)


    def draw_text_with_special_chars(
        draw, text, pos, font, special_font, color, line_spacing=10
    ):
        x, y = pos
        for char in text:
            if char == "\n":
                x = pos[0]
                y += font.size + line_spacing
                continue
            current_font = special_font if char in {"@", "_"} else font
            draw.text((x, y), char, font=current_font, fill=color)
            bbox = draw.textbbox((x, y), char, font=current_font)
            x = bbox[2]  


    draw_text_with_special_chars(
        draw, main_nick, (main_nick_x, main_nick_y), main_nick_font, special_font, text_color
    )
    draw_text_with_special_chars(
        draw, sub_nick, (sub_nick_x, sub_nick_y), sub_nick_font, special_font, text_color
    )
    draw_text_with_special_chars(
        draw,
        description,
        (description_x, description_y),
        description_font,
        special_font,
        text_color,
        line_spacing=10,
    )
    draw_text_with_special_chars(
        draw, twitter_username, (twitter_username_x, twitter_username_y), twitter_font, special_font, text_color
    )

 
    character = Image.open(character_path)
    character = character.resize((480, 480))
    banner.paste(character, (character_x, character_y), character)


    logo1 = Image.open(logo1_path).resize((logo1_width, logo1_height))
    banner.paste(logo1, (logo1_x, logo1_y), logo1)

    logo2 = Image.open(logo2_path).resize((logo2_width, logo2_height))
    banner.paste(logo2, (logo2_x, logo2_y), logo2)


    draw.line(
        (line1_x, line1_y, line1_x2, line1_y), fill=line1_color, width=line1_width
    )
    draw.line(
        (line2_x, line2_y, line2_x2, line2_y), fill=line2_color, width=line2_width
    )


    banner.convert("RGB").save(output_path, "JPEG", quality=100)

