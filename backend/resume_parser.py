import pdfplumber

def parse_resume(path):
    text=""
    with pdfplumber.open(path) as pdf:
        for p in pdf.pages:
            t=p.extract_text()
            if t: text+=t
    return text[:4000] if text else "No resume text."
