# -*- coding: utf-8 -*-
"""
hackathon peren

premières soumissions
"""


import pandas as pd

df = pd.read_csv("dataset.csv")

df["restaurant"]= df.start_lat.astype(str) + df.start_lon.astype(str)

def truncate(n):
    if n < 6:
        return n
    return 6


df1 = df[["restaurant", "fee"]].groupby("restaurant").nunique()
df1["prix_unique"] = (df1.fee == 1).astype(int)
df1["tronque"] = df1["fee"].apply(truncate)


merged = df[["observation_uuid", "restaurant"]].merge(df1, on="restaurant")

# algo = nombre de prix différents
v0 = merged[["observation_uuid","fee"]]
v0.columns = ["observation_uuid", "algorithm"]
v0.to_csv("soumission.csv", index=False)

# algo = prix unique vs multi prix
v0 = merged[["observation_uuid","prix_unique"]]
v0.columns = ["observation_uuid", "algorithm"]
v0.to_csv("soumission_01.csv", index=False)

# algo = nb de prix tronqué à 5
v0 = merged[["observation_uuid","tronque"]]
v0.columns = ["observation_uuid", "algorithm"]
v0.to_csv("soumission_02.csv", index=False)

