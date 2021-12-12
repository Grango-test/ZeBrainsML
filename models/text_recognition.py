from easyocr import Reader
import argparse
import cv2


def get_ocr(filename):
    image = cv2.imread(filename)

    reader = Reader(lang_list=['en', 'ru'])
    results = reader.readtext(image)
    return ' '.join([i[1] for i in results])
