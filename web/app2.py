from flask import Flask, render_template, request
import os
import pytube
import logging
from datetime import datetime

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "uploads"  # Carpeta de destino por defecto
app.config["ALLOWED_EXTENSIONS"] = {"mp4", "webm"}

# Configuración del registro
logs_folder = "logs"
os.makedirs(logs_folder, exist_ok=True)

log_filename = os.path.join(logs_folder, "descargas.log")
logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        formato = request.form["formato"]
        calidad = request.form["calidad"]
        carpeta_destino = request.form["carpeta_destino"]

        # Descargar el video y obtener la ruta de descarga
        descarga = descargar_video(url, carpeta_destino, formato, calidad)

        if descarga:
            log_info = f"Descargado: {descarga} - URL: {url} - Formato: {formato} - Calidad: {calidad}"
            logging.info(log_info)

            return render_template("index.html", mensaje="Descarga completada", ruta=descarga)
        else:
            return render_template("index.html", mensaje="Error en la descarga", ruta=None)

    return render_template("index.html", mensaje=None, ruta=None)

def descargar_video(url, carpeta_destino, formato, calidad):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.filter(file_extension=formato, res=calidad).first()
        if stream:
            # Combinar la carpeta de destino seleccionada con el nombre del archivo
            descarga = os.path.join(carpeta_destino, stream.title + "." + formato)
            stream.download(carpeta_destino)
            return descarga
        else:
            return None
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
