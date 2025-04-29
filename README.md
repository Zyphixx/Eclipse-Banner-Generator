# 📦 Banner Generator

A simple and beautiful banner generator built with [Streamlit](https://streamlit.io).  
Users can upload their own character image, choose styles, enter nicknames, descriptions, and generate high-quality banners automatically.

---

## ✨ Features

- Upload your own PNG, JPG, WebP, or BMP image
- Automatic background removal (powered by AI)
- Smart detection: transparent images are left untouched
- Clean character outline for dark/green themes
- 3 color styles: **Black**, **Green**, **Light Green**
- Custom nickname, subtitle, description, and Twitter handle
- Download the final banner in high quality

---

## 📁 How to run locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/banner-generator.git
cd banner-generator
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 📂 Folder structure

```
banner-generator/
├── app.py
├── generate_banner.py
├── border_picture.py
├── requirements.txt
├── fonts/
│   ├── barlow.ttf
│   ├── alpina.otf
│   ├── atlas.otf
│   └── MYRIADPRO-REGULAR.otf
├── logos/
│   ├── eclipse_light.png
│   ├── eclipse_dark.png
│   ├── asc_light.png
│   └── asc_dark.png
```

---

## 🙌 Credits

Built by **BuzzMalx** — feel free to contribute or suggest features!