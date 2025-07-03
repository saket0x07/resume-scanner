"""
File Name   : ranker.py
Description : Ranks resumes based on similarity scores and scales them to percentage.
Author      : Saket [github.com/saket0x07]
Date Created: 2025-07-03
Last Updated: 2025-07-03
Version     : 1.0.0

Notes       : Outputs sorted rankings from highest to lowest match quality.
"""


def rank_resumes(similarity_scores):
    """
    similarity_scores: list of tuples (resume_name, similarity_score)
    returns: sorted list from best to worst match (in percentage)
    """
    # Convert score to percentage and round
    percent_scores = [(name, round(score * 100, 2)) for name, score in similarity_scores]

    # Sort by descending similarity
    ranked = sorted(percent_scores, key=lambda x: x[1], reverse=True)
    return ranked
