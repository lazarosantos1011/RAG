from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Modelo de embedding
modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Textos simulando documento
documentos = [
    "RAG significa Retrieval-Augmented Generation.",
    "APIs permitem comunicação entre sistemas.",
    "O céu é azul devido à dispersão da luz.",
    "RAG combina sistemas de recuperação de informação "
    "com modelos de geração para criar respostas mais precisas.",
    "Embeddings transformam texto em vetores numéricos.",
    "Ollama permite rodar LLMs localmente."
]

# Gerar embeddings
embeddings = modelo.encode(documentos)

# Converter para float32 (requisito do FAISS)
embeddings = np.array(embeddings).astype("float32")

# Criar índice FAISS
dimensao = embeddings.shape[1]
index = faiss.IndexFlatL2(dimensao)

index.add(embeddings)

print("Documentos indexados:", index.ntotal)

query = "O que é RAG?"
query_embedding = modelo.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

k = 2 # Número de resultados
distances, indices = index.search(query_embedding, k)

print("Resultados mais próximos: ")
for i in indices[0]:
    print("-", documentos[i])