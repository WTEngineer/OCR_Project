from manga_ocr import MangaOcr

mocr = MangaOcr()

def recognize_text(image_path):
    return mocr(image_path)