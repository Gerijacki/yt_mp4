import os
import pytube
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')  # Aplicar un tema más sobrio

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

# Diseño de la interfaz de usuario con PySimpleGUI
formatos = ["mp4", "webm"]
calidades = ["144p", "240p", "360p", "480p", "720p", "1080p"]

layout = [
    [sg.Text("Descargador de YouTube", font=("Helvetica", 24), justification='center', relief=sg.RELIEF_RIDGE)],
    [sg.Text("URL del Video", font=("Helvetica", 14)), sg.InputText(key="-URL-", size=(30, 1), font=("Helvetica", 14))],
    [sg.Text("Carpeta de Destino", font=("Helvetica", 14)), sg.InputText(key="-CARPETA-", font=("Helvetica", 14)), sg.FolderBrowse()],
    [sg.Text("Formato del Video", font=("Helvetica", 14)), sg.Combo(formatos, default_value="mp4", key="-FORMATO-", font=("Helvetica", 14))],
    [sg.Text("Calidad del Video", font=("Helvetica", 14)), sg.Combo(calidades, default_value="720p", key="-CALIDAD-", font=("Helvetica", 14))],
    [sg.Button("Descargar", font=("Helvetica", 14), size=(15, 1)), sg.Button("Salir", font=("Helvetica", 14), size=(15, 1))],
    [sg.Text("", size=(30, 1), font=("Helvetica", 14), key="-OUTPUT-", justification='center')]  # Mensaje de salida
]

window = sg.Window("Descargador de YouTube", layout, background_color='#F0F0F0', resizable=True, element_justification='c')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Salir":
        break
    elif event == "Descargar":
        # Obtener valores de la interfaz
        url = values["-URL-"]
        carpeta_destino = values["-CARPETA-"]
        formato = values["-FORMATO-"]
        calidad = values["-CALIDAD-"]

        # Lógica de descarga aquí y actualizar el mensaje de salida
        descargar_video(url, carpeta_destino, formato, calidad)
        window["-OUTPUT-"].update("Descarga iniciada. Video guardado en: ruta_del_video.mp4")

window.close()
