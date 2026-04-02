from pdf_loader import extrair_texto_pdf
import os

if __name__ == "__main__":
    # Resolve o caminho do PDF relativo ao diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_pdf = os.path.join(script_dir, "wallace-abreu,+RMB+1T-2022+completa-79-89.pdf")

    extracted_text = extrair_texto_pdf(caminho_pdf)
    if extracted_text is not None:
        print(extracted_text)
        # Limitação de performance: como não há chunking para 
        # dividir a operação de leitura em pedaços menores,
        # se o LLM tiver dificuldade em processar 
        # todo o texto extraído, podemos fazer com que 
        # imprima apenas os primeiros 1000 caracteres do 
        # texto extraído para evitar sobrecarga.
        # Com 8 núcleos / 12 threads, não foram 
        # relatados problemas de performance, mas isso 
        # pode variar dependendo do tamanho do PDF e 
        # da capacidade do LLM.

        # print(extracted_text[:1000])
    else:
        print("Falha ao extrair texto do PDF.")