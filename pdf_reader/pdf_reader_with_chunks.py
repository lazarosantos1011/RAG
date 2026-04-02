from pdf_loader import extrair_texto_pdf
from chunking import chunk_text
import os

if __name__ == "__main__":
    # Resolve o caminho do PDF relativo ao diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_pdf = os.path.join(script_dir, "wallace-abreu,+RMB+1T-2022+completa-79-89.pdf")

    extracted_text = extrair_texto_pdf(caminho_pdf)
    chunks = chunk_text(extracted_text)
    
    if extracted_text is not None:
        # Há chunking para dividir a operação de leitura 
        # em pedaços menores, o que tende a melhorar a 
        # performance do LLM ao processar o texto 
        # extraído, especialmente para PDFs grandes
        print("Quantidade de chunks gerados:", len(chunks))
        print("\nPrimeiro chunk:\n")
        print(chunks[0])
    else:
        print("Falha ao extrair texto do PDF.")