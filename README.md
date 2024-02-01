<div align="center">

# Img to Text Converter

Este proyecto es un programa en Python que convierte archivos PDF compuestos por imágenes o imágenes individuales en un PDF con texto plano.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Nicolastolinii/Img_to_Text)](https://github.com/Nicolastolinii/Img_to_Text/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Nicolastolinii/Img_to_Text)](https://github.com/Nicolastolinii/Img_to_Text/pulls)

</div>

## Características Principales

- 📄 Convierte PDFs compuestos por imágenes en un PDF con texto plano.
- 🖼️ Permite convertir imágenes individuales en un PDF con texto.

## Requisitos del Sistema

- **Python 3.x**
- **Bibliotecas Python:**([ver requisitos detallados](requirements.txt))
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler - Página Oficial](https://poppler.freedesktop.org/)
### El programa admite los siguientes formatos:
- .JPG
- .JPEG
- .PNG
- .PDF
  
## Instalación

1. Clona el repositorio o descarga el código fuente.

```bash
git clone https://github.com/Nicolastolinii/Img_to_Text.git
cd Img_to_Text
```
### Instala las Dependencias.
```
pip install -r requirements.txt
```
## Uso desde la Línea de Comandos
```
python main.py "ruta a la imagen o PDF"
```
## Ejecutar la API con Interfaz de Usuario (Flask y Drag-and-Drop)

Además de la ejecución desde la línea de comandos, puedes utilizar la interfaz de usuario proporcionada mediante una API . Sigue estos pasos:

- Ejecuta la API.(en el directorio 'img_to_text/api')
```
python app.py
```
 Esto iniciará la aplicación Flask en http://localhost:5000.
- Accede a la Interfaz de Usuario.
 Abre "index.html" que se encuentra en la carpeta "api" Aquí encontrarás una interfaz amigable que admite la funcionalidad de arrastrar y soltar para procesar imágenes y PDFs.

## Build Docker
  Deje configurado un Dockerfile para levantar un Docker con el proyecto
### Crear imagen
```bash
docker build -t nombre_de_tu_imagen .
```
### Run Docker
```bash
docker run --rm --name "nombre del contenedor" nombre_de_tu_imagen

```

## Funciones Principales
```
preprocess_image(img)
```
Preprocesa una imagen antes de la extracción de texto. Realiza los siguientes pasos:

- Convierte la imagen a formato BGR.
- Ajusta el tamaño de la imagen (aumenta en un factor de 1.5).
- Aplica un desenfoque mediano a la imagen.
```
img_string(img)
```
Realiza la extracción de texto de una imagen preprocesada utilizando la biblioteca Tesseract.

#Configuración del Entorno: Tesseract OCR y Poppler
## Configuración de Tesseract OCR
Asegúrate de tener Tesseract OCR instalado en tu sistema y configurado correctamente. Puedes encontrar más información sobre la instalacion y configuración en la [la documentación oficial de Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
**Instalación en sistemas basados en Debian/Ubuntu:**
```
sudo apt-get update
sudo apt-get install tesseract-ocr
```
**Instalación en sistemas basados en Windows:**
Descarga el instalador desde la página de descargas de Tesseract OCR y sigue las instrucciones de instalación.
## Configuración de Poppler
En la sección "Downloads" o "Descargas", encontrarás enlaces a las versiones más recientes y la documentación asociada. Allí podrás obtener la versión específica de Poppler que necesitas para tu sistema. Si estás utilizando un sistema basado en Linux, es probable que puedas instalar Poppler directamente desde los repositorios de tu distribución.
```
sudo apt-get update
sudo apt-get install poppler-utils
```
Para sistemas Windows, puedes descargar los binarios desde la página oficial.


<div align="center">

  
  # Asegúrate de que tanto Tesseract OCR como Poppler estén correctamente agregados al PATH de tu sistema.
  
</div>



