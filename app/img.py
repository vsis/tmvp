from PIL import Image
import pytesseract
import os

def image_to_string(image_path, lang='spa'):
    return pytesseract.image_to_string(Image.open(image_path), lang=lang)

def proc_image(image_path, lang='spa'):
    str_data = image_to_string(image_path, lang)
    os.remove(image_path)
    return str_data
