from pdf_reader.pdf_loader import extrair_texto_pdf
from pdf_reader.chunking import chunk_text
from vector_store_phase2 import gerar_embeddings, criar_indice, salvar_indice
from config import CHUNK_SIZE, CHUNK_OVERLAP

def indexar_pdf(caminho_pdf):
    texto = extrair_texto_pdf(caminho_pdf)
    chunks = chunk_text(
        texto, 
        chunk_size=CHUNK_SIZE, 
        overlap=CHUNK_OVERLAP
    )

    embeddings = gerar_embeddings(chunks)
    index = criar_indice(embeddings)

    salvar_indice(index, chunks)

    print("Documento indexado com sucesso.")