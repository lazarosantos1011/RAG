from pypdf import PdfReader

def extrair_texto_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = ""

        for page in reader.pages:
            full_text += page.extract_text() + "\n"
            
        return full_text
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None