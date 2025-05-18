import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
import numpy as np

from meeseeks_ocr.ocr_task import preprocess_image

class TestRunOCR(unittest.TestCase):
    @patch('meeseeks_ocr.ocr_task.convert_from_path')
    @patch('meeseeks_ocr.ocr_task.pytesseract.image_to_string')
    def test_run_ocr(self, mock_image_to_string, mock_convert_from_path):
        # Setup mock return values
        mock_image = MagicMock(spec=Image.Image)
        mock_convert_from_path.return_value = [mock_image]
        mock_image_to_string.return_value = "Test OCR output"

        # Run the function
        from meeseeks_ocr.ocr_task import run_ocr
        result = run_ocr("test.pdf")

        # Verify results
        mock_convert_from_path.assert_called_once_with("test.pdf", dpi=300)
        mock_image_to_string.assert_called_once()
        self.assertEqual(result, "=== Page 1 === \nTest OCR output")

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_image_returns_pil_image(self):
        # Create a simple white dummy image (RGB, 100x100)
        dummy_img = Image.fromarray(np.full((100, 100, 3), 255, dtype=np.uint8))

        # Run preprocessing
        processed = preprocess_image(dummy_img)

        # Check type
        self.assertIsInstance(processed, Image.Image)

        # Check size increased (due to resize step fx=1.5)
        self.assertGreater(processed.size[0], dummy_img.size[0])
        self.assertGreater(processed.size[1], dummy_img.size[1])

