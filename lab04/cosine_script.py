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

pairs = []
n = len(names)

for a in range(n):
    for b in range(a + 1, n):
        pairs.append((similarity_matrix[a, b], a, b))

pairs_sorted = sorted(pairs, reverse=True)

first_diff = None
for sim, a, b in pairs_sorted:
    if sim < 0.9999: 
        first_diff = (sim, a, b)
        break

print("\nPereche cu similaritate mare:")
if first_diff:
    sim, a, b = first_diff
    print(f"- {names[a]}  <->  {names[b]}   sim = {sim:.4f}")
else:
    print("Nu exista perechi cu similarity < 1.00.")