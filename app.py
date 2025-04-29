import streamlit as st
from PIL import Image
import os
import io
from rembg import remove

from generate_banner import create_banner
from border_picture import add_outline

st.set_page_config(page_title="Banner Generator", layout="wide")
st.title("Banner Generator")


uploaded_file = st.file_uploader(
    "Upload your character image", type=["png", "jpg", "jpeg", "webp", "bmp", "tiff"]
)

nickname_main = st.text_input("Main nickname")
nickname_add = st.text_input("Additional nickname")
description = st.text_area("Description")
twitter_handle = st.text_input("Twitter handle (e.g., @buzzmalx)")
color_scheme = st.selectbox("Choose a color theme", ["Black", "Green", "Light Green"])


def remove_background_if_needed(pil_image):
    if pil_image.mode != "RGBA":
        pil_image = pil_image.convert("RGBA")

    alpha = pil_image.getchannel("A")
    alpha_data = alpha.getdata()
    total_pixels = alpha.size[0] * alpha.size[1]
    fully_opaque_pixels = sum(1 for pixel in alpha_data if pixel == 255)
    fully_transparent_pixels = sum(1 for pixel in alpha_data if pixel == 0)

    if fully_transparent_pixels > 0 and fully_opaque_pixels < total_pixels * 0.9:
        return pil_image
    else:
        img_bytes = io.BytesIO()
        pil_image.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()
        output = remove(img_bytes)
        return Image.open(io.BytesIO(output)).convert("RGBA")


if st.button("Generate banner"):
    if uploaded_file is not None:
        raw_image = Image.open(uploaded_file).convert("RGBA")
        image = remove_background_if_needed(raw_image)

        character_path = "temp_character.png"
        bg_color = "#000000"
        text_color = "#5bfe9c"
        logo1 = "logos/eclipse_light.png"
        logo2 = "logos/asc_light.png"
        logo2_size = (110, 45)
        logo2_position = (180, 87)

        if color_scheme == "Black":
            outlined_image = add_outline(image, (91, 254, 156, 255), 4)
            outlined_image.save(character_path)

        elif color_scheme == "Green":
            outlined_image = add_outline(image, (91, 254, 156, 255), 4)
            outlined_image.save(character_path)
            bg_color = "#5bfe9c"
            text_color = "#000000"
            logo1 = "logos/eclipse_dark.png"
            logo2 = "logos/asc_dark.png"
            logo2_size = (90, 87)
            logo2_position = (180, 65)

        elif color_scheme == "Light Green":
            character_path = "temp_character_light.png"
            image.resize((480, 480)).save(character_path)
            bg_color = "#dcffcd"
            text_color = "#000000"
            logo1 = "logos/eclipse_dark.png"
            logo2 = "logos/asc_dark.png"
            logo2_size = (90, 87)
            logo2_position = (180, 65)

        output_path = "generated_banner.jpg"

        create_banner(
            background_color=bg_color,
            text_color=text_color,
            main_nick=nickname_main,
            main_nick_x=901,
            main_nick_y=84,
            sub_nick=nickname_add,
            sub_nick_x=901,
            sub_nick_y=200,
            description=description,
            description_x=911,
            description_y=381,
            twitter_username=twitter_handle,
            twitter_username_x=911,
            twitter_username_y=64,
            character_path=character_path,
            character_x=312,
            character_y=20,
            logo1_path=logo1,
            logo1_x=62,
            logo1_y=65,
            logo1_width=90,
            logo1_height=87,
            logo2_path=logo2,
            logo2_x=logo2_position[0],
            logo2_y=logo2_position[1],
            logo2_width=logo2_size[0],
            logo2_height=logo2_size[1],
            output_path=output_path,
            line1_x=901,
            line1_x2=1350,
            line1_y=99,
            line1_color=text_color,
            line1_width=1,
            line2_x=901,
            line2_x2=1350,
            line2_y=359,
            line2_color=text_color,
            line2_width=1,
        )

        banner = Image.open(output_path)
        st.image(banner, caption="Your generated banner", use_column_width=True)

        with open(output_path, "rb") as file:
            st.download_button(
                label="Download banner",
                data=file,
                file_name="banner.jpg",
                mime="image/jpeg",
            )

        for temp_file in [
            "temp_character.png",
            "temp_character_light.png",
            output_path,
        ]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    else:
        st.error("Please upload an image first.")
