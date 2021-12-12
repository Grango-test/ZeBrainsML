try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def get_ocr(image_path):
    img = Image.open(image_path)
    res = pytesseract.image_to_string(image_path)
    return res
