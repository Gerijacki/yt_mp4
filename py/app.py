import os
import pytube
import PySimpleGUI as sg

def descargar_video(url, carpeta_destino, formato, calidad):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.filter(file_extension=formato, res=calidad).first()
        if stream:
            descarga = stream.download(carpeta_destino)
            sg.popup("Descarga completada", f"Video guardado en: {descarga}")
        else:
            sg.popup_error("No se encontró una corriente con el formato y calidad seleccionados.")
    except Exception as e:
        sg.popup_error(f"Error al descargar el video: {e}")

# Interfaz de Usuario con PySimpleGUI
formatos = ["mp4", "webm"]
calidades = ["144p", "240p", "360p", "480p", "720p", "1080p"]
layout = [
    [sg.Text("URL del Video"), sg.InputText(key="-URL-")],
    [sg.Text("Carpeta de Destino"), sg.InputText(key="-CARPETA-"), sg.FolderBrowse()],
    [sg.Text("Formato del Video"), sg.Combo(formatos, default_value="mp4", key="-FORMATO-")],
    [sg.Text("Calidad del Video"), sg.Combo(calidades, default_value="720p", key="-CALIDAD-")],
    [sg.Button("Descargar"), sg.Button("Salir")]
]

window = sg.Window("Descargador de YouTube", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Salir":
        break
    elif event == "Descargar":
        url = values["-URL-"]
        carpeta_destino = values["-CARPETA-"]
        formato = values["-FORMATO-"]
        calidad = values["-CALIDAD-"]
        if url and carpeta_destino:
            descargar_video(url, carpeta_destino, formato, calidad)
        else:
            sg.popup_error("Por favor, ingresa el URL del video y la carpeta de destino.")

window.close()
