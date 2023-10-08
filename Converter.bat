@echo off

:: Descarrega i instal·la Python
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

:: Actualitza pip
python -m pip install --upgrade pip

:: Instal·la les llibreries
pip install os pytube pysimplegui

:: Executa l'arxiu Python youtube_to_mp4.py
python youtube_to_mp4.py

:: Elimina l'arxiu d'instal·lació de Python
del python-installer.exe

