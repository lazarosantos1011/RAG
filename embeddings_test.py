from sentence_transformers import SentenceTransformer

import numpy as np

modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

sentencas = [
    "O gato está dormindo.",
    "Um felino descansa no sofá.",
    "O carro está quebrado."
]

embeddings = modelo.encode(sentencas)

print("Dimensão do vetor", embeddings[0].shape)

# Teste de similaridade simples (por prod. escalar)
similaridade = np.dot(embeddings[0], embeddings[1])
print("Similaridade entre frase 1 e 2: ", similaridade)

similaridade = np.dot(embeddings[0], embeddings[2])
print("Similaridade entre frase 2 e 3: ", similaridade)
