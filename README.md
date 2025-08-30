# Audio Downloader (yt-dlp + Typer)

Herramienta de línea de comandos para descargar audio (MP3 192 kbps) desde enlaces compatibles con **yt-dlp** (YouTube y muchos más).  
Incluye barra de progreso y dos comandos: **descargar un solo enlace** o **varios desde un archivo**.

---

## 🚀 Requisitos

- **Python**: >= 3.11 (probado con 3.11 y 3.13)  
- **FFmpeg**: necesario para convertir a MP3  
  - Debian/Ubuntu: `sudo apt-get install ffmpeg`  
  - Arch: `sudo pacman -S ffmpeg`  
  - Fedora: `sudo dnf install ffmpeg`  
- **Dependencias Python**: `yt-dlp`, `typer`, `tqdm`

---

## ⚙️ Instalación rápida

(Opcional) Crear y activar entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instalar dependencias:
``` bash
pip install yt-dlp typer tqdm
```
    ℹ️ Nota: Hay un pyproject.toml, pero no se expone aún un paquete instalable con entrypoint. Ejecuta el script directamente.

📌 Uso

Script principal: download_audio.py (usa Typer).
🔹 Descargar un solo audio

python download_audio.py descargar-audio "URL" [CARPETA_DESTINO] [--playlist/--no-playlist]

Ejemplo:

python download_audio.py descargar-audio "https://www.youtube.com/watch?v=XXXX"

🔹 Descargar audios desde un archivo (una URL por línea)

python download_audio.py descargar-audios-de-archivo RUTA_ARCHIVO [CARPETA_DESTINO] [--playlist/--no-playlist]

Ejemplo:

python download_audio.py descargar-audios-de-archivo videos.txt

📄 Formato de videos.txt

    Una URL por línea.

    Se ignoran líneas en blanco.

Ejemplo:

https://youtu.be/VIDEO_ID1
https://youtu.be/VIDEO_ID2

📂 Salida y ubicación de descarga

    Por defecto, si no indicas CARPETA_DESTINO, el script crea/usa:

    /home/david/Music/downloaded_audios

    Puedes sobreescribirla pasando CARPETA_DESTINO.

    Nombre del archivo: %(title)s.mp3

    Calidad: MP3 a 192 kbps (convertido con FFmpeg).

    Playlists: por defecto deshabilitadas (--no-playlist). Usa --playlist si quieres descargar listas completas.

⚡ Ejemplos rápidos

# Un solo audio a carpeta por defecto
```bash
python download_audio.py descargar-audio "https://youtu.be/VIDEO_ID"
```
# Un solo audio a carpeta personalizada
```bash
python download_audio.py descargar-audio "https://youtu.be/VIDEO_ID" /ruta/a/mis_audios
```
# Varios audios desde archivo
```bash
python download_audio.py descargar-audios-de-archivo videos.txt /ruta/a/mis_audios
```
# Descargar playlist completa desde archivo
```bash
python download_audio.py descargar-audios-de-archivo videos.txt --playlist
```

🛠️ Solución de problemas

    FFmpeg no encontrado → instala FFmpeg y valida con ffmpeg -version.

    Permiso al crear carpeta por defecto → pasa una carpeta destino propia.

    Barra de progreso no avanza → puede ser conexión lenta o falta de total_bytes; reintenta.

    URLs de playlist → por defecto solo descarga el video, usa --playlist para descargar la lista completa.

📦 Dependencias declaradas

En pyproject.toml:
```tolm
[project]
requires-python = ">=3.11"
dependencies = [
  "tqdm",
  "typer",
  "yt-dlp"
]
```
