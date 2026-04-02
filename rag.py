import numpy as np
from sentence_transformers import SentenceTransformer
from vector_store_phase2 import carregar_indice
from llm import perguntar_llm
from config import TOP_K
import time

modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

index, chunks = carregar_indice()

def buscar_contexto(pergunta):
    pergunta_embedding = modelo.encode([pergunta])
    distancias, indices = index.search(np.array(pergunta_embedding), TOP_K)

    resultados = [chunks[i] for i in indices[0]]
    return "\n\n".join(resultados)

def montar_prompt(contexto, pergunta):
    return f"""
    Responda sempre mencionando meu nome primeiro, que é "Lázaro".
    Responda APENAS com base no contexto abaixo.
    Se não estiver no contexto, diga que não encontrou.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}

    Resposta:
    Lázaro, (responda aqui)
    """
    
def responder(pergunta):
    t0 = time.time()

    contexto = buscar_contexto(pergunta)
    t1 = time.time()

    prompt = montar_prompt(contexto, pergunta)
    t2 = time.time()

    resposta = perguntar_llm(prompt)
    t3 = time.time()

    print("Tempo busca:", t1 - t0)
    print("Tempo prompt:", t2 - t1)
    print("Tempo LLM:", t3 - t2)
    print("Tempo total:", t3 - t0)

    return resposta