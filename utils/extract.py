"""
File Name   : extract.py
Description : Handles text extraction from DOCX, PDF, and TXT files.
Author      : Saket [github.com/saket0x07]
Date Created: 2025-07-03
Last Updated: 2025-07-03
Version     : 1.0.0

Notes       : Uses docx2txt and PyMuPDF (fitz) for content parsing.
"""

import docx2txt
import fitz  # PyMuPDF

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text(file):
    file_type = file.type
    if "pdf" in file_type:
        return extract_text_from_pdf(file)
    elif "word" in file_type or "docx" in file.name:
        return extract_text_from_docx(file)
    elif "text" in file_type or file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return ""
