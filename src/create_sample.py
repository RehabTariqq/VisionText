from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


# Get the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Create the input folder if it does not exist
INPUT_DIR = BASE_DIR / "input"
INPUT_DIR.mkdir(exist_ok=True)


# Create a white image
image = Image.new("RGB", (1000, 700), "white")

draw = ImageDraw.Draw(image)


# Windows Arial font
font_path = "C:/Windows/Fonts/arial.ttf"

title_font = ImageFont.truetype(font_path, 42)
normal_font = ImageFont.truetype(font_path, 28)
small_font = ImageFont.truetype(font_path, 24)


# Title
draw.text(
    (60, 50),
    "VISIONTEXT DEMO DOCUMENT",
    fill="black",
    font=title_font
)


# Document information
draw.text(
    (60, 140),
    "Document ID: VT-0042",
    fill="black",
    font=normal_font
)

draw.text(
    (60, 190),
    "Date: 02-10-2026",
    fill="black",
    font=normal_font
)

draw.text(
    (60, 260),
    "Name: Rehab",
    fill="black",
    font=normal_font
)

draw.text(
    (60, 330),
    "Project: AI Image Recognition",
    fill="black",
    font=normal_font
)

draw.text(
    (60, 390),
    "Technology: OpenCV and Tesseract OCR",
    fill="black",
    font=normal_font
)

draw.text(
    (60, 450),
    "Status: Successfully Processed",
    fill="black",
    font=normal_font
)


# Final message
draw.text(
    (60, 550),
    "VISIONTEXT OCR TEST",
    fill="black",
    font=title_font
)

draw.text(
    (60, 620),
    "Image to machine-readable text.",
    fill="black",
    font=small_font
)


# Save the image
output_path = INPUT_DIR / "sample_document.png"

image.save(output_path)

print("Sample image created successfully!")
print(f"Saved to: {output_path}")