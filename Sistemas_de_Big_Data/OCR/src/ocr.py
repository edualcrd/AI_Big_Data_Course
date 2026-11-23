
from pathlib import Path

import pytesseract
from PIL import Image
from pytesseract import Output

# Ruta del ejecutable Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# Esta función reconoce el texto de una imagen ya procesada utilizando Tesseract.
def extract_text(image, lang="eng", psm=6): # Utilizo --psm 6 para que Tesseract trate la imagen como un solo bloque de texto.
    # Args:
        # image: Imagen procesada mediante OpenCV.
        # lang: Idioma del reconocimiento.
        # psm: Modo de segmentación de página de Tesseract.

    # Returns:
        # Texto reconocido.
    


    # Convertir el array de OpenCV a imagen PIL
    pil_image = Image.fromarray(image)

    # Configuración del motor OCR
    config = f"--oem 3 --psm {psm}"

    # Reconocimiento de texto
    text = pytesseract.image_to_string(pil_image, lang=lang, config=config)
    return text.strip()

    # Esta función calcula la confianza media de las palabras reconocidas.
def get_ocr_confidence(image, lang="eng", psm=6):
    
    # Returns:
        # Diccionario con confianza media y número de palabras.
    
    pil_image = Image.fromarray(image)
    config = f"--oem 3 --psm {psm}"

    data = pytesseract.image_to_data(pil_image, lang=lang,config=config, output_type=Output.DICT)

    confidences = []
    recognized_words = 0

    for word, confidence in zip(data["text"], data["conf"]):

        if word.strip() and float(confidence) >= 0:
            confidences.append(float(confidence))
            recognized_words += 1

    if confidences:
        average_confidence = round(sum(confidences) / len(confidences), 2)
    else:
        average_confidence = 0.0

    return {"average_confidence": average_confidence, "recognized_words": recognized_words}

# Y esta guarda el texto reconocido en un archivo TXT.
def save_text(text, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(text, encoding="utf-8")

## La confianza que devuelve tesserac es una estimación del reconocimiento no una garantía de que el texto sea 100% correcto.abs

