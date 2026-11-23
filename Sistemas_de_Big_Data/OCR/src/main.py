import csv
from pathlib import Path

from src.ocr import clean_text, extract_text, get_ocr_confidence, save_text
from src.preprocessing import load_image, preprocess_image, save_processed_image
from src.structuring import extract_apollo_timeline_events, structure_text_lines

# Directorios del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

ORIGINAL_DIR = PROJECT_ROOT / "data" / "original"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Imagen seleccionada para el proyecto
IMAGE_NAME = "apollo 11 ascent timeline.webp"


def main():

    # Crear directorios de salida
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Comprobar que existe la imagen seleccionada
    image_path = ORIGINAL_DIR / IMAGE_NAME

    if not image_path.is_file():
        raise FileNotFoundError(f"No se encontró la imagen: {image_path}")

    print(f"\nProcesando imagen: {IMAGE_NAME}")

    # Cargar imagen original
    original = load_image(image_path)

    # Preprocesamiento con OpenCV
    processed = preprocess_image(original)

    # Guardamos la imagen procesada
    processed_path = save_processed_image(processed, image_path, PROCESSED_DIR)

    #Extraemos texto mediante OCR
    raw_text = extract_text(processed, lang="eng")

    # Limpiamos y normalizamos el texto
    cleaned_text = clean_text(raw_text)

    # Calculamos la confianza del reconocimiento
    metrics = get_ocr_confidence(processed, lang="eng")

    # Guardardamos texto extraído en TXT
    text_path = OUTPUT_DIR / "resultado.txt"
    save_text(cleaned_text, text_path)

    # Preparar resultados generales
    results = [{"imagen": IMAGE_NAME, "imagen_procesada": processed_path.name, "palabras_reconocidas": metrics["recognized_words"], "confianza_media": metrics["average_confidence"], "texto_original": raw_text, "texto_limpio": cleaned_text, "error": ""}]

    # Exportamos los  resultados generales a CSV
    csv_path = OUTPUT_DIR / "resultados.csv"

    fieldnames = ["imagen", "imagen_procesada", "palabras_reconocidas", "confianza_media", "texto_original", "texto_limpio", "error"]

    with csv_path.open("w", newline="", encoding="utf-8-sig") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    # Estructuraramos el texto OCR por líneas
    line_records = structure_text_lines(results)

    line_csv_path = OUTPUT_DIR / "resultados_lineas.csv"

    line_fieldnames = ["imagen", "numero_linea", "confianza_media_imagen", "texto_linea"]

    with line_csv_path.open("w", newline="", encoding="utf-8-sig") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=line_fieldnames)

        writer.writeheader()
        writer.writerows(line_records)

    # Extraemos eventos de la cronología Apollo 11
    apollo_events = extract_apollo_timeline_events(line_records)

    # Exportar eventos estructurados
    events_csv_path = OUTPUT_DIR / "apollo11_eventos.csv"

    event_fieldnames = ["imagen", "numero_linea", "tiempo", "codigo", "descripcion", "confianza_media_imagen", "texto_original"]

    with events_csv_path.open("w",newline="",encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=event_fieldnames)
        writer.writeheader()
        writer.writerows(apollo_events)

    # Mostramos el resumen final
    print("\n RESUMEN FINAL ")
    print(f"Imagen procesada: {IMAGE_NAME}")
    print(f"Palabras reconocidas: {metrics['recognized_words']}")
    print(f"Confianza media: {metrics['average_confidence']}%")
    print(f"Líneas estructuradas: {len(line_records)}")
    print(f"Eventos Apollo 11 extraídos: {len(apollo_events)}")

    print("\nArchivos generados:")
    print(f"Imagen procesada: {processed_path}")
    print(f"Texto extraído: {text_path}")
    print(f"CSV general: {csv_path}")
    print(f"CSV por líneas: {line_csv_path}")
    print(f"CSV de eventos: {events_csv_path}")


if __name__ == "__main__":
    main()
