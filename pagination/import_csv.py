import pandas as pd

file_path = 'Popular_Baby_Names.csv'

# Lire le fichier CSV
df = pd.read_csv(file_path)

# Afficher les 20 premières lignes du DataFrame
print(df.head(20))
