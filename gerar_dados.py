from sklearn.datasets import fetch_california_housing
import pandas as pd

# pega o dataset do sklearn e salva como csv pra deixar no repo
dados = fetch_california_housing(as_frame=True)
df = dados.frame
df.to_csv("california_housing.csv", index=False)

print("base salva:", df.shape)
print(df.head())
