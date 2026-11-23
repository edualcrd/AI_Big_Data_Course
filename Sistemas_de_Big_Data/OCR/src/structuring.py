# Convierte los textos OCR de cada imagen en registros individuales, conservando el número de línea y la imagen de procedencia.
def structure_text_lines(results):

    records = []

    for result in results:

        # Ignorar las imágenes que hayan producido algúnos errores
        if result.get("error"):
            continue

        text = result.get("texto_limpio", "")

        # Separar el texto en líneas
        lines = text.splitlines()

        for line_number, line in enumerate(lines, start=1):

            # Normalizar espacios
            clean_line = " ".join(line.split())

            # Ignorar líneas vacías
            if not clean_line:
                continue

            records.append({"imagen": result["imagen"], "numero_linea": line_number, "confianza_media_imagen": result["confianza_media"], "texto_linea": clean_line})

    return records
