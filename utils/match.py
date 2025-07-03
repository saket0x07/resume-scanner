"""
File Name   : match.py
Description : Computes semantic similarity between job description and resumes using SpaCy.
Author      : Saket [github.com/saket0x07]
Date Created: 2025-07-03
Last Updated: 2025-07-03
Version     : 1.0.0

Notes       : Uses 'en_core_web_md' SpaCy model for vector-based similarity. Ensure it's downloaded.
"""

import spacy

# Load SpaCy's medium English model (make sure to install it first)
nlp = spacy.load("en_core_web_md")

def compute_similarity(doc1_text, doc2_text):
    doc1 = nlp(doc1_text)
    doc2 = nlp(doc2_text)
    return doc1.similarity(doc2)
