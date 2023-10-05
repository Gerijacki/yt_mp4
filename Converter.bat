@echo off

echo Descargando Python...
curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

echo Instalando Python...
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_launcher=0

echo Actualizando pip...
python -m ensurepip --upgrade

echo Instalando las librerías desde requirements.txt...
pip install -r requirements.txt

echo Ejecutando el código Python...
python youtube_to_mp4.py

echo Limpieza...
del python-installer.exe

echo Proceso completado. Presiona cualquier tecla para salir.
pause >nul
