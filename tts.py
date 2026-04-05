from datetime import datetime
import subprocess
import unicodedata
import os
import sys
import threading
import time
import simpleaudio as sa

PIPER_PATH = r"C:\piper\piper.exe"
MODEL_PATH = r"C:\piper\models\pt_BR-edresson-low.onnx"

def normalizar_texto(texto):
    return unicodedata.normalize("NFC", texto)

# Sintetizador de voz usando o Piper
def falar(texto):
    texto = normalizar_texto(texto)

    # Criar diretório se não existir
    os.makedirs("output_audio", exist_ok=True)

    # Criar nome único com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    arquivo_saida = f"output_audio/saida_{timestamp}.wav"
    
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

    # Tocar o áudio de forma nativa e assíncrona (não precisa de threading)
    if os.name == "nt":
        import winsound
        winsound.PlaySound(arquivo_saida, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        # Se for Linux/Mac
        threading.Thread(target=tocar_audio, args=(arquivo_saida,), daemon=True).start()

def tocar_audio(caminho):
    try:
        if os.name == "posix":
            subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", caminho])
    except Exception as e:
        print(f"Erro ao tocar áudio: {e}")
