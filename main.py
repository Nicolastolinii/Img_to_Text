from modules.pdf_converter import pdf_img

if __name__ == "__main__":
    input_path = "test.pdf"  # Reemplaza con la ruta de tu PDF de imágenes
    name = input_path.split('.')[0]
    output_pdf_path = (f"{name}_convert.pdf")  # Ruta de salida del PDF de texto
    pdf_img(input_path, output_pdf_path)