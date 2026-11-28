import pandas as pd
import numpy as np
file = pd.read_csv('anime-dataset-2023.csv',na_values='UNKNOWN')
anime= file[['Name','Genres',"Score"]]
print(anime)
anime=anime.dropna(subset=['Score','Genres'])
print(anime)
anime['Score']=anime['Score'].astype(float)
anime['Genres']=anime['Genres'].str.split(', ')
anime = anime.explode('Genres')
anime=anime.groupby('Genres')["Score"].mean().sort_values(ascending=False)
print(anime)

