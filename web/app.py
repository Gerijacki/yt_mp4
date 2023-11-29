from flask import Flask, render_template, request, send_file
import os
import pytube

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "uploads"  # Carpeta de destino por defecto
app.config["ALLOWED_EXTENSIONS"] = {"mp4", "webm"}

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

        return render_template("index.html", mensaje="Descarga completada", ruta=descarga)

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
