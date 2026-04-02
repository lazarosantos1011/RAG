import sounddevice as sd
from scipy.io.wavfile import write

def gravar_audio(nome_arquivo="entrada.wav", duracao=5, fs=16000):
    print(f"Gravando por {duracao} segundos...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()
    write(nome_arquivo, fs, audio)
    print(f"Áudio salvo como {nome_arquivo}")

if __name__ == "__main__":
    gravar_audio()