import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from typing import Dict, List, Tuple


TRACK_DIR = "./data/track_0_10000.csv"
ARTIST_DIR= "./data/artist_0_10000.csv"


def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_track = pd.read_csv(TRACK_DIR)
    df_artist= pd.read_csv(ARTIST_DIR)
    
    df_track.set_index(keys="id", inplace = True)
    df_artist.set_index(keys="id", inplace=True)
    
    df_track.drop(columns='Unnamed: 0', inplace=True)
    df_artist.drop(columns='Unnamed: 0', inplace=True)
    
    return df_track, df_artist


df_track, df_artist = load_data()


df_track.head()


df_artist.head()


df_track.info()


df_artist.info()


df_01 = df_track[["available_markets", "popularity"]].dropna()


df_01["available_markets"] = df_01["available_markets"].apply(lambda x : x.split(","))


df_01


all_areas = df_01["available_markets"].explode().unique()

for a in all_areas:
    df_01[f"in_{a}"] = df_01["available_markets"].apply(lambda x : a in x)

cor    = df_01.corrwith(df_01.popularity).drop("popularity")
mean   = df_01.mean().drop("popularity")


result = pd.concat({"correlate": cor, "percent": mean}, axis=1)
result.nlargest(10, columns=["correlate"])


result.describe()


plt.figure(figsize=(16, 8))
ax = plt.subplot(1, 3, 1)
sns.boxplot(df_01["in_ME"], df_01["popularity"], ax=ax)
ax = plt.subplot(1, 3, 2)
sns.boxplot(df_01["in_RS"], df_01["popularity"], ax=ax)
ax = plt.subplot(1, 3, 3)
sns.boxplot(df_01["in_XK"], df_01["popularity"], ax=ax);






