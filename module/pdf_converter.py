import fitz
from PIL import Image
from pdf2image import convert_from_path
from tqdm import tqdm
from .image_processing import img_string

def pdf_img(input_path):
    text_content = []

    try:
        if input_path.lower().endswith('.pdf'):
            images = convert_from_path(input_path)

            if not images:
                raise ValueError("No se pudieron convertir imágenes desde el archivo PDF.")

            doc = fitz.open()

            # Barra de progreso estilizada
            bar = tqdm(total=len(images), desc="Conviertiendo PDF", unit="image", dynamic_ncols=True)

            for i, image in enumerate(images):
                text = img_string(image)
                text_content.append(text)

                # Añade una nueva página al documento de salida
                page = doc.new_page(width=image.width, height=image.height)

                # Inserta texto en la página
                text_position = 50
                line_spacing = 20
                for line in text.split('\n'):
                    page.insert_text((50, text_position), line, fontsize=17, color=(0, 0, 0))
                    text_position += line_spacing

                # Añade una línea separadora después del texto
                line_position = text_position + 10
                line_width = 500
                page.draw_line((50, line_position), (50 + line_width, line_position), color=(0, 0, 0), width=1)
                bar.update(1)

        elif input_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images = [Image.open(input_path)]

            if not images:
                raise ValueError("No se pudo abrir la imagen.")

            # Barra de progreso estilizada
            bar = tqdm(total=1, desc="Converting Image", unit="image", dynamic_ncols=True)
            print("Conviertiendo imagen:")
            doc = fitz.open()
            text = img_string(images[0])
            text_content.append(text)

            # Añade una nueva página al documento de salida
            page = doc.new_page(width=images[0].width, height=images[0].height)

            # Inserta texto en la página
            text_position = 50
            line_spacing = 20
            for line in text.split('\n'):
                page.insert_text((50, text_position), line, fontsize=17, color=(0, 0, 0))
                text_position += line_spacing

            # Añade una línea separadora después del texto
            line_position = text_position + 10
            line_width = 500
            page.draw_line((50, line_position), (50 + line_width, line_position), color=(0, 0, 0), width=1)
            bar.update(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"
    finally:
        if 'bar' in locals():
            bar.close()

    if not text_content:
        return "No se generaron páginas en el documento."

    result = doc.write()
    doc.close()
    print("\n¡Proceso completado!")
    return result
