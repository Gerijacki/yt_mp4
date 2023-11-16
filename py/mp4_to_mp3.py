import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from tkinter import Tk, Label, Button, StringVar, filedialog

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

# Crear la interfaz gráfica
root = Tk()
root.title("Convertidor MP4 a MP3")

input_path_var = StringVar()

Label(root, text="Seleccionar archivo MP4:", font="Helvetica 14").pack(pady=10)
Button(root, text="Seleccionar", command=seleccionar_archivo).pack(pady=5)

Button(root, text="Convertir a MP3", command=convertir).pack(pady=10)

output_label = Label(root, text="", font="Helvetica 12 bold")
output_label.pack(pady=10)

root.mainloop()
