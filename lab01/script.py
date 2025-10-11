import pandas as pd

df = pd.read_csv("imdb_top.csv")
df[:1000].to_csv("imdb_top_1000.csv", index=False)