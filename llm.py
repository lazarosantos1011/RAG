import requests
import time
from config import MODEL_NAME

def perguntar_llm(prompt):
    URL = "http://localhost:11434/api/generate"

    inicio = time.time()

    response = requests.post(URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    fim = time.time()
    print(f"Tempo de resposta do LLM: {fim - inicio:.2f} segundos.")

    try:
        return response.json()["response"]
    except Exception as e:
        print("Erro ao obter resposta do LLM:", e, "Resposta do servidor: ", response.text)
        return "Desculpe, ocorreu um erro ao obter a resposta do modelo."