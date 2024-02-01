# Usa una imagen base de Python
FROM python:3.8

# Instala Tesseract OCR y Poppler
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y poppler-utils \
    && apt-get install -y libgl1-mesa-glx 

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias de la aplicación, incluyendo tu módulo
RUN pip install --no-cache-dir -r requirements.txt 

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

