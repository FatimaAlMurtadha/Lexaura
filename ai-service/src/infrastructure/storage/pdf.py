from pypdf import PdfReader

# pdf -> text -> chunks -> embeddings -> chromaDB -> query -> retrieve -> LLM -> answer
# 1. pdf -> text

def extract_text_from_pdf(file_obj) -> str:
    reader = PdfReader(file_obj)
    pages_text = [] # an empty container to hold the text of all pages

    for page in reader.pages:
        text = page.extract_text() or ""
        pages_text.append(text)

        # clean
        cleaned = "\n".join(
            line.strip()
            for line in "\n".join(pages_text).splitlines()
            if line.strip()
        )
    return cleaned

