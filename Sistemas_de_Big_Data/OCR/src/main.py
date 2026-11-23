import csv
from pathlib import Path

import matplotlib.pyplot as plt
from src.ocr import extract_text, get_ocr_confidence, save_text
from src.preprocessing import load_image, preprocess_image, save_processed_image

# Directorio principal del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Imagen que vamos a analizar
IMAGE_NAME = "apollo 11 ascent timeline.webp"


def main():

    # Cargar la imagen original
    image_path = PROJECT_ROOT / "data" / "original" / IMAGE_NAME
    original = load_image(image_path)

    # Preprocesar la imagen
    processed = preprocess_image(original)

    # Guardar la imagen procesada
    processed_path = save_processed_image(processed, image_path, PROJECT_ROOT / "data" / "processed")

    print(f"\nImagen procesada: {processed_path.name}")

    # Extraer el texto mediante OCR
    text = extract_text(processed, lang="eng")

    # Calcular la confianza de el reconocimiento
    metrics = get_ocr_confidence(processed, lang="eng")

    # Guardar el texto en TXT
    output_dir = PROJECT_ROOT / "output"

    txt_path = output_dir / f"{Path(IMAGE_NAME).stem}.txt"
    save_text(text, txt_path)

    # Exportar los resultados a formato CSV.
    csv_path = output_dir / "resultados.csv"

    with csv_path.open("w", newline="", encoding="utf-8-sig") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=["imagen", "palabras_reconocidas", "confianza_media","texto"])

        writer.writeheader()

        writer.writerow({"imagen": IMAGE_NAME, "palabras_reconocidas": metrics["recognized_words"], "confianza_media": metrics["average_confidence"], "texto": text})

    # Mostramos los resultados
    print("\n RESULTADOS OCR")
    print(f"Palabras reconocidas: {metrics['recognized_words']}")
    print(f"Confianza media: {metrics['average_confidence']}%")

    print("\nTexto extraído:")
    print(text)

    print("\nArchivos generados:")
    print(f"TXT: {txt_path}")
    print(f"CSV: {csv_path}")

    # Visualizamos la imagen procesada
    plt.figure(figsize=(12, 8))
    plt.imshow(processed, cmap="gray")
    plt.title("Imagen preprocesada")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
