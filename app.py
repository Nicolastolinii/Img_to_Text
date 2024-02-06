
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from module.pdf_converter import pdf_img
import tempfile
from models import db
from utils import check_user_request_limit
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, db)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

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

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
    
@app.route('/process', methods=['POST'])
def process_in_endpoint():
    #Asegura que la solicitud incluya un archivo
    if 'file' not in request.files or request.files['file'] is None:
        return jsonify({'error': 'No se proporcionó un archivo'}), 400
    user_ip = request.remote_addr
    if not check_user_request_limit(user_ip):
        return jsonify({'error': 'Límite de solicitudes alcanzado para este usuario'}), 429
    archivo = request.files['file']
    #Verifica que el archivo tenga una extension permitida
    extension_permitida = ['pdf', 'png', 'jpg', 'jpeg']
    file_extension = archivo.filename.rsplit('.', 1)[-1].lower()
    if file_extension not in extension_permitida:
        return jsonify({'error': 'Formato de archivo no permitido'}), 400
    
    file_content = archivo.read()
    temp_file_path = save_file(file_content, file_extension)
    #Procesa el archivo y retorna el resultado en formato PDF
    res = process_file(temp_file_path)
    if res:
        return res
    else:
        return jsonify({'error': 'Error al procesar el archivo'}), 500
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)