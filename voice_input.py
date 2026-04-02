import sounddevice as sd
from scipy.io.wavfile import write
import whisper

fs = 16000 # Sample rate
modelo = whisper.load_model("small") #trocar para "small" ou "medium" se quiser melhor acurácia, mas vai demorar mais

def gravar(duracao=8, arquivo_saida="entrada.wav"):
    print("Fale agora...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait() # Espera até a gravação ser concluída
    write(arquivo_saida, fs, audio) # Salva o áudio em um arquivo WAV
    print("Gravação concluída e salva como", arquivo_saida)

def ouvir():
    gravar()
    resultado = modelo.transcribe("entrada.wav", language="pt")
    return resultado["text"]

if __name__ == "__main__":
    texto = ouvir()
    print("Você disse: ", texto)