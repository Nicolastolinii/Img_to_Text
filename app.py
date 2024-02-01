
import os
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify
from flask_cors import CORS
from module.pdf_converter import pdf_img
import tempfile

app = Flask(__name__)
CORS(app)
def save_file(file_content, file_extension):
    # Crea un archivo temporal con una extensión específica
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_extension}')
    # Escribe el contenido del archivo en el archivo temporal
    temp_file.write(file_content)
    temp_file.close()
    return temp_file.name

def process_file(temp_file_path):
    # Procesa el archivo y retorna el resultado en formato PDF
    result = pdf_img(temp_file_path)
    os.remove(temp_file_path)
    return result

@app.route('/process', methods=['POST'])
def process_in_endpoint():
    #Asegura que la solicitud incluya un archivo
    if 'file' not in request.files or request.files['file'] is None:
        return jsonify({'error': 'No se proporcionó un archivo'}), 400
    
    archivo = request.files['file']
    #Verifica que el archivo tenga una extension permitida
    extension_permitida = ['pdf', 'png', 'jpg', 'jpeg']
    file_extension = archivo.filename.rsplit('.', 1)[-1].lower()
    if file_extension not in extension_permitida:
        return jsonify({'error': 'Formato de archivo no permitido'}), 400
    file_content = archivo.read()
    temp_file_path = save_file(file_content, file_extension)
    #Procesa el archivo y retorna el resultado en formato PDF
    with ThreadPoolExecutor() as executor:
        future = executor.submit(process_file, temp_file_path)
        res = future.result()  # Espera a que la tarea en hilo termine

    return res
if __name__ == '__main__':
    app.run(debug=True)