import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from tkinter import Tk, Label, Button, StringVar, filedialog
import PySimpleGUI as sg
import pytube

def convertir_a_mp3(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path, codec="mp3")

def seleccionar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos MP4", "*.mp4")])
    input_path_var.set(file_path)

def convertir():
    input_path = input_path_var.get()
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Archivos MP3", "*.mp3")])
        try:
            convertir_a_mp3(input_path, output_path)
            output_label.config(text=f"Conversión completa. Audio guardado en: {output_path}", foreground="green")
        except Exception as e:
            output_label.config(text=f"Error durante la conversión: {e}", foreground="red")
    else:
        output_label.config(text="Selecciona un archivo MP4 primero.", foreground="red")

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

# Crear la interfaz gráfica
root = Tk()
root.title("Convertidor MP4 a MP3")

input_path_var = StringVar()

Label(root, text="Seleccionar archivo MP4:", font="Helvetica 14").pack(pady=10)
Button(root, text="Seleccionar", command=seleccionar_archivo).pack(pady=5)

Button(root, text="Convertir a MP3", command=convertir).pack(pady=10)

output_label = Label(root, text="", font="Helvetica 12 bold")
output_label.pack(pady=10)

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
        # Lógica de descarga aquí y actualizar el mensaje de salida
        window["-OUTPUT-"].update("Descarga iniciada. Video guardado en: ruta_del_video.mp4")

window.close()
