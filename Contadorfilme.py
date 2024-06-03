
import altair as alt
import pandas as pd


df_marvel_full = pd.read_csv('Data/Custo_Lucro.csv')

#df_marvel_filme_lucro = df_marvel_full[['Filmes',"Lucro"]]
#print(df_marvel_filme_lucro)
df_marvel_filme_lucro_sorted=df_marvel_full.sort_values(by=['L'], ascending=False)
print(df_marvel_filme_lucro_sorted)
    


