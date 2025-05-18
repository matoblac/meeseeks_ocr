from pdf2image import convert_from_path
import pytesseract
from PIL import Image

## Preproccesing
import cv2
import numpy as np

def preprocess_image(pil_image: Image.Image) -> np.ndarray:
    """
    Preprocesses an image for OCR.

    Args:
        pil_image (Image.Image): Input image.

    Returns:
        np.ndarray: Preprocessed image.
    """
    # Convert PIL image to numpy array
    img = np.array(pil_image)
    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Step 1: Remove noise
    img = cv2.GaussianBlur(img, (3, 3), 0)

    # Step 2: Adaptive thresholding
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Step 3: Resize up
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Step 4: Dilation and make charaters bolder
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    return Image.fromarray(img)



def run_ocr(input_file: str) -> str:
    """
    Runs OCR on a scanned PDF and returns the full extracted text as a string.

    Args:
        input_file (str): Path to the PDF file.

    Returns:
        str: OCR output (text) from all pages.
    """
    try:
        # Convert PDF to images
        image = convert_from_path(input_file, dpi=300)
    except Exception as e:
        raise RuntimeError(f"Failed to convert PDF to images: {e}")

    ocr_output = []

    # Iterate through each page image
    # enumerate(image) starts from page 1
    for page_num, image in enumerate(image, start=1):
        try:
            # Preprocess the image
            # Convert the image to a format suitable for OCR
            image = preprocess_image(image)


            # oem 1 tells tesseract to use LSTM OCR engine
            # psm 6 assumes a single uniform block of text
            custom_config = r'--oem 1 --psm 6'

            # Perform OCR on the image
            text = pytesseract.image_to_string(image, lang='eng', config=custom_config)
            # Append the OCR result to the output list
            # Append the page number and text to the output
            ocr_output.append(f"=== Page {page_num} === \n{text.strip()}")
        except Exception as e:
            raise RuntimeError(f"Failed to perform OCR on page {page_num}: {e}")
    return "\n".join(ocr_output)

