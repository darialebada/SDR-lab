import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# get similarity matrix from lab04
sim_df = pd.read_csv("../lab04/similarity_matrix.csv", index_col=0)

item_names = sim_df.index.tolist()
similarity_matrix = sim_df.values

np.fill_diagonal(similarity_matrix, 0.0)
similarity_matrix[similarity_matrix >= 0.9999] = 0.0

# ---------------------------
# Example User–Item Matrix
# Rows = Users, Columns = Items
# Ratings: 1 = picked, 0 = not picked (can also use real ratings)
# ---------------------------
NUM_USERS = 5
NUM_ITEMS = len(item_names)
NUM_MAX_LIKES_PER_USER = 10

user_item_matrix = np.zeros((NUM_USERS, NUM_ITEMS), dtype=float)

rng = np.random.default_rng()

for user_id in range(NUM_USERS):
    liked_count = rng.integers(2, NUM_MAX_LIKES_PER_USER + 1)
    liked_items = rng.choice(NUM_ITEMS, size=liked_count, replace=False)
    user_item_matrix[user_id, liked_items] = 1.0

print("Liked items per user:")
for user_id in range(NUM_USERS):
    liked_items = np.where(user_item_matrix[user_id] == 1)[0]
    liked_item_names = [item_names[i] for i in liked_items]
    print(f"- user_{user_id}: {liked_item_names}")

# ---------------------------
# Recommend items for a user
# ---------------------------
def recommend_items(user_id, user_item_matrix, item_similarity, top_k=2):
    user_ratings = user_item_matrix[user_id]
    
    # Predicted scores are weighted sum of similar items user already interacted with
    scores = user_ratings @ item_similarity
    
    # Exclude items already chosen
    scores[user_ratings == 1] = -1
    
    recommended_items = np.argsort(scores)[::-1][:top_k]
    return recommended_items, scores


TARGET_USER = 0

recommended_items, scores = recommend_items(
    user_id=TARGET_USER,
    user_item_matrix=user_item_matrix,
    item_similarity=similarity_matrix,
    top_k=5,
)

print(f"\nUSER-{TARGET_USER}:")
print(f"\n--------------------------------------")

sorted_indices = np.argsort(scores)[::-1]
print(f"\nPredicted scores:")
for idx in sorted_indices[:-1]:
    print(f"{item_names[idx]} -> {scores[idx]:.4f}")

print(f"\nRecommended Items:")
for idx in recommended_items:
    print(f"- {item_names[idx]} -> {scores[idx]:.4f}")
