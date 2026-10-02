# VisionText — AI Image-to-Text Recognition5

VisionText is a basic AI-powered Optical Character Recognition (OCR) pipeline that converts text from images into machine-readable text.


---

##  Overview

VisionText takes a document image as input, preprocesses the image using OpenCV, and extracts readable text using Tesseract OCR.

The pipeline demonstrates a simple image-to-text workflow:

**Input Image → Grayscale → Gaussian Blur → Adaptive Thresholding → Tesseract OCR → Confidence Validation → Annotated Output**

---

##  Features

* Image input processing
* Grayscale conversion
* Gaussian blur preprocessing
* Adaptive thresholding
* Tesseract OCR integration
* OCR confidence calculation
* 80% confidence validation threshold
* Text extraction into a `.txt` file
* OCR bounding-box visualization
* Intermediate preprocessing outputs

---

##  How It Works

### 1. Image Input

The system reads a document image from the `input` folder.

### 2. Grayscale Conversion

The RGB image is converted into grayscale to simplify the image before OCR processing.

### 3. Gaussian Blur

Gaussian blur is applied to reduce small amounts of image noise.

### 4. Adaptive Thresholding

The grayscale image is converted into a high-contrast binary representation to improve text visibility.

### 5. OCR

Tesseract OCR processes the preprocessed image and extracts machine-readable text.

### 6. Confidence Validation

The OCR confidence values are analyzed to calculate the average confidence of the extracted text.

The project uses an **80% validation threshold**.

### 7. Output Generation

The pipeline produces:

* Grayscale image
* Thresholded image
* Annotated image with detected text regions
* Extracted text file

---

##  Validation Result

The sample document was successfully processed with:

| Metric             |     Result |
| ------------------ | ---------: |
| OCR Confidence     | **94.79%** |
| Required Threshold |    **80%** |
| Validation         | **PASSED** |

The sample therefore exceeded the required OCR confidence threshold.

---

##  Technologies

* **Python**
* **OpenCV**
* **Tesseract OCR**
* **pytesseract**
* **Pillow**
* **NumPy**

---

## 📁 Project Structure

```text
VisionText/
│
├── input/
│   └── sample_document.png
│
├── outputs/
│   ├── grayscale.png
│   ├── thresholded.png
│   ├── annotated.png
│   └── recognized_text.txt
│
├── src/
│   ├── create_sample.py
│   └── ocr_pipeline.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone <https://github.com/RehabTariqq/VisionText>
cd VisionText
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

##  Tesseract OCR

VisionText uses **Tesseract OCR** for text recognition.

On Windows, Tesseract must be installed separately.

The current development setup uses:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If Tesseract is installed in another location, update the Tesseract executable path in `ocr_pipeline.py`.

---

## ▶ Running VisionText

First generate the sample document:

```powershell
python src/create_sample.py
```

Then run the OCR pipeline:

```powershell
python src/ocr_pipeline.py
```

The processed files will be generated inside:

```text
outputs/
```

---

##  Outputs

### `grayscale.png`

Grayscale version of the input image.

### `thresholded.png`

Preprocessed image after adaptive thresholding.

### `annotated.png`

Image containing OCR-detected text regions and bounding boxes.

### `recognized_text.txt`

Machine-readable text extracted from the document.

---

##  Project Goal

The goal of VisionText is to demonstrate the integration of computer vision preprocessing and OCR into a simple, reproducible AI pipeline.

Rather than training a new OCR model, the project focuses on **model/library integration, preprocessing, validation, and output generation**.

---

##  Future Improvements

Possible future improvements include:

* Support for user-provided images through command-line arguments
* Multiple image format support
* Improved preprocessing for noisy documents
* OCR language selection
* PDF document support
* Web interface for uploading images
* More detailed OCR confidence reporting
* Automatic text-region visualization
* Docker-based deployment

---

##  Author

**Rehab Tariq**

Computer Science Student
Artificial Intelligence / AI Engineering

*Developed as part of the DecodeLabs Artificial Intelligence Internship — Batch 2026*.
