from pathlib import Path

import matplotlib.pyplot as plt
from src.preprocessing import load_image, preprocess_image, save_processed_image

# Directorio principal del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Primera imagen de prueba
IMAGE_NAME = "apollo 11 ascent timeline.webp"


def main():
    # Ruta de la imagen original
    image_path = PROJECT_ROOT / "data" / "original" / IMAGE_NAME

    # Cargar imagen
    original = load_image(image_path)
    # Preprocesar la imagen
    processed = preprocess_image(original)

    # Guardar el resultado
    output_path = save_processed_image(processed, image_path, PROJECT_ROOT / "data" / "processed")
    print(f"Imagen procesada correctamente: {output_path}")

    # Visualizar el resultado
    plt.figure(figsize=(12, 8))
    plt.imshow(processed, cmap="gray")
    plt.title("Imagen preprocesada")
    plt.axis("off")
    plt.show()


if __name__ == "__main__": 
    main()
