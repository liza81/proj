from docx import Document

def extract_headings(doc_path, font_size=12):
    doc = Document(doc_path)
    headings = []
    
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            if paragraph.runs:  
                first_run = paragraph.runs[0]
                if first_run.font.size and first_run.font.size.pt == font_size: 
                    headings.append(paragraph.text.strip())
    
    return headings

doc_path = "reviews1.docx"
headings = extract_headings(doc_path)
print("Заголовки в документе reviews1.docx:")
for heading in headings:
    print(heading)