"""
File Name   : app.py
Description : Streamlit frontend for the Resume Scanner NLP application.
Author      : Saket [github.com/saket0x07]
Date Created: 2025-07-03
Last Updated: 2025-07-03
Version     : 1.0.0

Notes       : Provides UI for uploading job descriptions and resumes; connects backend utilities for parsing, matching, and ranking.
"""

import streamlit as st
from utils.extract import extract_text
from utils.preprocess import clean_text
from utils.match import compute_similarity
from utils.ranker import rank_resumes

st.set_page_config(page_title="Resume Scanner", layout="wide")

# App Title & Description
st.title("Resume Scanner 🔍")
st.markdown("""
Upload a job description and multiple resumes to find the best match using NLP techniques.
Built with SpaCy, NLTK, and Python. Let's simplify hiring decisions!
""")

# File Uploaders
jd_file = st.file_uploader("📜 Upload Job Description (TXT)", type=["txt"])
resume_files = st.file_uploader("📄 Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

# Status Message
if jd_file and resume_files:
    st.success("Files uploaded successfully! Ready to process...")

    # Extract job description text
    jd_text = extract_text(jd_file)

    # Store results
    similarity_scores = []

    # Loop through resumes
    for resume in resume_files:
        resume_text = extract_text(resume)
        score = compute_similarity(jd_text, resume_text)
        similarity_scores.append((resume.name, round(score, 3)))

    # Rank them
    ranked = rank_resumes(similarity_scores)

    # Display results
    st.subheader("📊 Ranking Results")
    for name, score in ranked:
        st.markdown(f"**{name}** — Similarity Score: `{score}`")

else:
    st.info("Please upload both job description and resumes to begin.")
