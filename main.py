from modulee.pdf_converter import pdf_img

if __name__ == "__main__":
    # Coloca la ruta de tu archivo PDF como argumento de la línea de comandos
    input_path = input("Ingrese la ruta del archivo PDF: ")
    
    try:
        # Llama a la función pdf_img y obtén el contenido del PDF
        resultado_pdf_content = pdf_img(input_path)
        name = input_path.split('.')[0]
        output_pdf_path = (f"{name}_convert.pdf")
        
        # Guarda el contenido del PDF en un nuevo archivo
        output_path = output_pdf_path
        with open(output_path, 'wb') as output_file:
            output_file.write(resultado_pdf_content)
        
        print(f"El PDF resultante se guardó con el nombre: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        
        