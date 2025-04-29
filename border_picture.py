from PIL import Image, ImageDraw

def add_outline(image, outline_color, outline_width):

    image = image.resize((480, 480), Image.LANCZOS)


    alpha = image.split()[-1]


    outline = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(outline)


    for x in range(-outline_width, outline_width + 1):
        for y in range(-outline_width, outline_width + 1):
            if x != 0 or y != 0:  
                draw.bitmap((x, y), alpha, fill=outline_color)


    result = Image.alpha_composite(outline, image)
    print("success ✅")
    return result


