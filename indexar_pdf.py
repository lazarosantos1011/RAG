import os
from indexer import indexar_pdf

if __name__ == "__main__":
    # Resolve o caminho do PDF relativo ao diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_pdf = os.path.join(
        script_dir, 
        "./data/Guia-PMBOK-7a-Edicao.pdf"
    )
    #caminho_pdf = "./pdf_reader/wallace-abreu,+RMB+1T-2022+completa-79-89.pdf"

    indexar_pdf(caminho_pdf)