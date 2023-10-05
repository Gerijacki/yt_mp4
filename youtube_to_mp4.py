import os
import pytube
import PySimpleGUI as sg

def descargar_video(url, carpeta_destino):
    try:
        video = pytube.YouTube(url)
        video.streams.filter(file_extension="mp4", progressive=True).first().download(carpeta_destino)
        sg.popup("Descarga completada", f"Video guardado en: {carpeta_destino}")
    except Exception as e:
        sg.popup_error(f"Error al descargar el video: {e}")

# Interfaz de Usuario con PySimpleGUI
layout = [
    [sg.Text("URL del Video"), sg.InputText(key="-URL-")],
    [sg.Text("Carpeta de Destino"), sg.InputText(key="-CARPETA-"), sg.FolderBrowse()],
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
        if url and carpeta_destino:
            descargar_video(url, carpeta_destino)
        else:
            sg.popup_error("Por favor, ingresa el URL del video y la carpeta de destino.")

window.close()
