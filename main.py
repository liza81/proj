from docx import Document
import os
from pprint import pprint

# TODO Хозяин! Не удовлетворяет требованию проекта. Все функции обработки должны быть в functions.py. Запуск кода в main.py
# TODO Объедини структуру проекта из ветки main с функциями текущей ветки
 
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


def load_titles(folder):
    headings = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames: 
            rel_path = os.path.join(dirpath, file)
            doc_path = os.path.abspath(rel_path)
            if os.path.isfile(doc_path):
                headings.extend(extract_headings(doc_path))
    return headings


# функция запуска
def main():
    pprint(load_titles('data'))


# Вызов
main()
