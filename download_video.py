import yt_dlp
import typer
from typing_extensions import Annotated
from tqdm import tqdm
import os

app = typer.Typer()

barras = {}


def progreso(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        descargado = d.get('downloaded_bytes', 0)

        if d['filename'] not in barras:
            barras[d['filename']] = tqdm(
                total=total,
                unit='B',
                unit_scale=True,
                desc=os.path.basename(d['filename']),
                ncols=80
            )
        barra = barras[d['filename']]
        barra.n = descargado
        barra.refresh()


def crear_carpeta_default():
    directory_name = "/home/david/Music/downloaded_audios"

    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
        return directory_name
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
        return directory_name
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


@app.command()
def descargar_audio(url: Annotated[str, typer.Argument()],
                    carpeta_destino: Annotated[str, typer.Argument()] = None):
    if not carpeta_destino:
        carpeta_destino = crear_carpeta_default()
    opciones = {
        "format": "bestaudio/best",
        "outtmpl": f"{carpeta_destino}/%(title)s.%(ext)s",
        "progress_hooks": [progreso],
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
    print("Descargado con exito!!!")


@app.command()
def descargar_audios_de_archivo(ruta_archivo: Annotated[str, typer.Argument()],
                                carpeta_destino: Annotated[str, typer.Argument()] = None):
    if not carpeta_destino:
        carpeta_destino = crear_carpeta_default()
    opciones = {
        "format": "bestaudio/best",
        "outtmpl": f"{carpeta_destino}/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with open(ruta_archivo) as f:
        enlaces = [x.strip() for x in f if x.strip()]

    with typer.progressbar(enlaces, label="Descargando audios") as barra:
        for url in barra:
            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])


if __name__ == "__main__":
    app()
