# 🔍 Resume Scanner using NLP

A smart resume scanner built with Python and NLP to parse and rank resumes based on their similarity to a given job description. Designed for recruiters and developers to simplify hiring decisions.

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-blue?logo=streamlit)
![SpaCy](https://img.shields.io/badge/NLP-SpaCy-green?logo=spacy)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)

---

## 🚀 Features

- 📂 Upload job descriptions and multiple resumes (PDF or DOCX)
- 🧠 Semantic matching using SpaCy's word vectors
- 📊 Resume ranking with similarity scores (scaled to %)
- 🧹 Text cleaning and preprocessing with NLTK
- ⚡ Intuitive Streamlit interface for instant insights

---

## 🧰 Tech Stack

| Layer         | Libraries / Tools     |
|---------------|-----------------------|
| Language      | Python                |
| NLP           | SpaCy, NLTK           |
| Parsing       | PyMuPDF, docx2txt     |
| Frontend UI   | Streamlit             |

---

## 📦 Installation

```bash
git clone https://github.com/saket0x07/resume-scanner.git
cd resume-scanner
pip install -r requirements.txt
python -m spacy download en_core_web_md
streamlit run app.py

---

## 📄 How It Works
Upload a job description in .txt format.
Upload one or more resumes in .pdf or .docx.
The app extracts and cleans the text, computes semantic similarity, and ranks resumes by relevance.
Results are displayed with percentage-based scores.

---

## Project Structure

resume-scanner/
├── app.py
├── requirements.txt
├── utils/
│   ├── extract.py
│   ├── preprocess.py
│   ├── match.py
│   └── ranker.py
├── components/
│   ├── sidebar.py
│   ├── display.py
│   └── loader.py
├── data/
│   ├── resumes/
│   └── job_descriptions/
├── assets/
│   ├── styles.css
│   └── logo.png
└── README.md


##
Author
Saket 👨‍💻 GitHub: @saket0x07 📅 Created: July 2025
