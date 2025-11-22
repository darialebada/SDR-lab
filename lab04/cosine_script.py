import json
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_html(text: str):
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()

# get data from file
with open("tesco_sample.json", encoding="utf-8") as f:
    data = json.load(f)

names = [p.get("name", f"prod_{i}") for i, p in enumerate(data)]
raw_descriptions = [p.get("description", "") for p in data]

# get rid of HTML tags and use only lowercase
descriptions = []
for d in raw_descriptions:
    cleaned = clean_html(d)
    descriptions.append(cleaned)

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(descriptions)

similarity_matrix = cosine_similarity(tfidf_matrix)

# save matrix to CSV
sim_df = pd.DataFrame(similarity_matrix, index=names, columns=names)
print(sim_df)
sim_df.to_csv("similarity_matrix.csv", encoding="utf-8")

# set diagonal to 0 to ignore self-similarity
np.fill_diagonal(similarity_matrix, 0.0)
similarity_matrix[similarity_matrix >= 0.9999] = 0.0

# find most similar pair (max value in matrix)
i, j = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)
best_sim = similarity_matrix[i, j]

print("Most similar products:")
print(f"  Product 1: {names[i]}")
print(f"  Product 2: {names[j]}")
print(f"  Cosine similarity: {best_sim:.4f}")
