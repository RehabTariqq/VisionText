import cv2
import pytesseract
from pathlib import Path


# ============================================================
# VisionText
# AI Image-to-Text Recognition System
# DecodeLabs Internship - Project 4
# ============================================================


# ------------------------------------------------------------
# 1. PROJECT PATHS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "outputs"

INPUT_IMAGE = INPUT_DIR / "sample_document.png"

GRAYSCALE_IMAGE = OUTPUT_DIR / "grayscale.png"
THRESHOLD_IMAGE = OUTPUT_DIR / "thresholded.png"
ANNOTATED_IMAGE = OUTPUT_DIR / "annotated.png"
TEXT_OUTPUT = OUTPUT_DIR / "recognized_text.txt"


# Create outputs folder if necessary
OUTPUT_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 2. TESSERACT CONFIGURATION
# ------------------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ------------------------------------------------------------
# 3. CHECK INPUT
# ------------------------------------------------------------

if not INPUT_IMAGE.exists():

    print("ERROR: Input image was not found.")

    print(f"Expected:")
    print(INPUT_IMAGE)

    raise SystemExit


print("=" * 65)
print("                     VISIONTEXT")
print("          AI IMAGE-TO-TEXT RECOGNITION")
print("=" * 65)


print()
print(f"Input image: {INPUT_IMAGE}")


# ------------------------------------------------------------
# 4. LOAD IMAGE
# ------------------------------------------------------------

image = cv2.imread(str(INPUT_IMAGE))


if image is None:

    print("ERROR: OpenCV could not read the image.")

    raise SystemExit


print("✓ Image loaded successfully")


# ------------------------------------------------------------
# 5. GRAYSCALE CONVERSION
# ------------------------------------------------------------

gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


cv2.imwrite(
    str(GRAYSCALE_IMAGE),
    gray
)


print("✓ Grayscale conversion completed")


# ------------------------------------------------------------
# 6. GAUSSIAN BLUR
# ------------------------------------------------------------

blurred = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)


print("✓ Gaussian blur completed")


# ------------------------------------------------------------
# 7. ADAPTIVE THRESHOLDING
# ------------------------------------------------------------

thresholded = cv2.adaptiveThreshold(
    blurred,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)


cv2.imwrite(
    str(THRESHOLD_IMAGE),
    thresholded
)


print("✓ Adaptive thresholding completed")


# ------------------------------------------------------------
# 8. OCR CONFIGURATION
# ------------------------------------------------------------

# PSM 6 treats the image as a block of text.

ocr_config = "--oem 3 --psm 6"


# ------------------------------------------------------------
# 9. EXTRACT TEXT
# ------------------------------------------------------------

recognized_text = pytesseract.image_to_string(
    thresholded,
    config=ocr_config
)


# ------------------------------------------------------------
# 10. GET OCR CONFIDENCE DATA
# ------------------------------------------------------------

data = pytesseract.image_to_data(
    thresholded,
    config=ocr_config,
    output_type=pytesseract.Output.DICT
)


confidence_values = []


for confidence in data["conf"]:

    try:

        value = float(confidence)

        if value >= 0:

            confidence_values.append(value)

    except ValueError:

        continue


# ------------------------------------------------------------
# 11. CALCULATE AVERAGE CONFIDENCE
# ------------------------------------------------------------

if len(confidence_values) > 0:

    average_confidence = (
        sum(confidence_values)
        / len(confidence_values)
    )

else:

    average_confidence = 0


# ------------------------------------------------------------
# 12. SAVE RECOGNIZED TEXT
# ------------------------------------------------------------

with open(
    TEXT_OUTPUT,
    "w",
    encoding="utf-8"
) as file:

    file.write("VISIONTEXT - RECOGNIZED TEXT\n")

    file.write("=" * 40)

    file.write("\n\n")

    file.write(
        recognized_text.strip()
    )


# ------------------------------------------------------------
# 13. CREATE ANNOTATED IMAGE
# ------------------------------------------------------------

annotated = image.copy()


for i in range(len(data["text"])):

    text = data["text"][i].strip()


    if text == "":
        continue


    try:

        confidence = float(
            data["conf"][i]
        )

    except ValueError:

        continue


    # Only annotate detections
    # with confidence >= 80%.

    if confidence >= 80:

        x = int(data["left"][i])
        y = int(data["top"][i])

        width = int(
            data["width"][i]
        )

        height = int(
            data["height"][i]
        )


        # Draw bounding box
        cv2.rectangle(
            annotated,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )


        # Add text and confidence
        label = (
            f"{text} "
            f"({confidence:.0f}%)"
        )


        cv2.putText(
            annotated,
            label,
            (x, max(y - 5, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 128, 0),
            2
        )


# ------------------------------------------------------------
# 14. SAVE ANNOTATED IMAGE
# ------------------------------------------------------------

cv2.imwrite(
    str(ANNOTATED_IMAGE),
    annotated
)


# ------------------------------------------------------------
# 15. DISPLAY RECOGNIZED TEXT
# ------------------------------------------------------------

print()
print("=" * 65)
print("                    RECOGNIZED TEXT")
print("=" * 65)

print()

print(
    recognized_text.strip()
)


# ------------------------------------------------------------
# 16. DISPLAY CONFIDENCE
# ------------------------------------------------------------

print()
print("=" * 65)
print("                  CONFIDENCE REPORT")
print("=" * 65)

print()

print(
    f"Average OCR Confidence: "
    f"{average_confidence:.2f}%"
)

print(
    "Validation Threshold: 80%"
)


# ------------------------------------------------------------
# 17. VALIDATION
# ------------------------------------------------------------

if average_confidence >= 80:

    print()
    print("✓ VALIDATION PASSED")

    print(
        "OCR confidence meets the "
        "80% project threshold."
    )

else:

    print()
    print("⚠ VALIDATION BELOW 80%")

    print(
        "Try using a clearer image "
        "or adjusting preprocessing."
    )


# ------------------------------------------------------------
# 18. OUTPUT SUMMARY
# ------------------------------------------------------------

print()
print("=" * 65)
print("                    OUTPUT FILES")
print("=" * 65)

print()

print(
    f"✓ Grayscale: {GRAYSCALE_IMAGE}"
)

print(
    f"✓ Thresholded: {THRESHOLD_IMAGE}"
)

print(
    f"✓ Annotated: {ANNOTATED_IMAGE}"
)

print(
    f"✓ Text: {TEXT_OUTPUT}"
)


print()
print("=" * 65)
print("                 VISIONTEXT COMPLETE")
print("=" * 65)