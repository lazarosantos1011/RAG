import subprocess
import unicodedata
import os
import sys
from playsound import playsound

PIPER_PATH = r"C:\piper\piper.exe"
MODEL_PATH = r"C:\piper\models\pt_BR-edresson-low.onnx"

def normalizar_texto(texto):
    return unicodedata.normalize("NFC", texto)

# Sintetizador de voz usando o Piper
def falar(texto, arquivo_saida="saida.wav"):
    texto = normalizar_texto(texto)

    comando = [
        PIPER_PATH,
        "--model", MODEL_PATH,
        "--output_file", arquivo_saida,
    ]

    processo = subprocess.Popen(
        comando,
        stdin=subprocess.PIPE,
        text=True
    )

    processo.communicate(input=texto)

    tocar_audio(arquivo_saida)

def tocar_audio(caminho):
    if os.name == "nt":  #Windows
        playsound(caminho)
    elif os.name == "posix":  #Linux/Mac # type: ignore
        subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", caminho])