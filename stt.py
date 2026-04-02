import whisper
import os

# Set FFmpeg path (adjust if your installation is in a different location)
os.environ["PATH"] += os.pathsep + r"C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin"  # if using manual installation

modelo = whisper.load_model("small") #trocar para "small" ou "medium" se quiser melhor acurácia, mas vai demorar mais

def transcrever_audio(caminho_audio):
    resultado = modelo.transcribe(caminho_audio, language="pt")
    return resultado["text"]

if __name__ == "__main__":
#    script_dir = os.path.dirname(os.path.abspath(__file__))
#    caminho_audio = os.path.join(
 #       script_dir, 
 #       "entrada.wav"
 #   )

    texto = transcrever_audio("entrada.wav")
    print("Texto transcrito: ", texto)
