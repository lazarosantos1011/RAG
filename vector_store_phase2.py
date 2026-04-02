import faiss
import numpy as np
import pickle 
from sentence_transformers import SentenceTransformer
from config import INDEX_PATH

modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def gerar_embeddings(textos):
    return modelo.encode(textos)

def criar_indice(embeddings):
    dimensions = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimensions)
    index.add(np.array(embeddings))
    return index

def salvar_indice(index, chunks):
    faiss.write_index(index, f"{INDEX_PATH}.faiss")
    with open(f"{INDEX_PATH}.pkl", "wb") as f:
        pickle.dump(chunks, f)

def carregar_indice():
    index = faiss.read_index(f"{INDEX_PATH}.faiss")
    with open(f"{INDEX_PATH}.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks