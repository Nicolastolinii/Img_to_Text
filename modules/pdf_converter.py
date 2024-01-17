import fitz
from PIL import Image
from pdf2image import convert_from_path
import progressbar
from modules.image_processing import  img_string

def pdf_img(input_path):
    text_content = []
    if input_path.lower().endswith('.pdf'):
        try:
            images = convert_from_path(input_path)  
        # Crea un nuevo documento de salida
            doc = fitz.open()
            #Barra de progreso estilizada
            bar = progressbar.ProgressBar(max_value=len(images), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            print("Conviertiendo PDF:")
            bar.start()
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
                bar.update(i + 1)
        except Exception as e:
            print(f"Error: {str(e)}")
    elif input_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        try:
            images = [Image.open(input_path)]
            #Barra de progreso estilizada
            bar = progressbar.ProgressBar(max_value=1, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            print("Conviertiendo PDF:")
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
        except Exception as e:
            print(f"Error:{str(e)}")
    bar.finish()
    result = doc.write()
    doc.close()
    print("\n¡Proceso completado!")
    return result