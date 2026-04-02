import os
import time
import numpy as np
from sentence_transformers import SentenceTransformer
from pdf_loader import extrair_texto_pdf
from chunking import chunk_text

def medir_tempo_sem_chunks(model, texto):
    start = time.time()
    embedding = model.encode([texto])
    end = time.time()
    return end - start

def medir_tempo_com_chunks(model, texto):
    chunks = chunk_text(texto, chunk_size=5000, overlap=100)
    
    start = time.time()
    embeddings = model.encode(chunks)
    end = time.time()
    
    return end - start, len(chunks)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_pdf = os.path.join(script_dir, "Portugues-All-Bible-Corrigida-Fiel.pdf")  # coloque aqui seu PDF

    texto = extrair_texto_pdf(caminho_pdf)

    if texto is None:
        print("Erro ao ler PDF.")
        exit()

    print("Carregando modelo de embedding...")
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    print("\n🔹 Testando sem chunks...")
    tempo_sem = medir_tempo_sem_chunks(model, texto)
    print(f"Tempo sem chunking: {tempo_sem:.2f} segundos")

    print("\n🔹 Testando com chunks...")
    tempo_com, qtd_chunks = medir_tempo_com_chunks(model, texto)
    print(f"Tempo com chunking: {tempo_com:.2f} segundos")
    print(f"Quantidade de chunks: {qtd_chunks}")

    print("\n📊 Comparação:")
    if tempo_com < tempo_sem:
        print("Chunking foi mais rápido.")
    else:
        print("Chunking foi mais lento (mas pode ser mais estável para LLMs).")