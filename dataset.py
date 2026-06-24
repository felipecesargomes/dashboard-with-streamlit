import json
import pandas as pd

file = open('data/vendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)
df['data_compra'] = pd.to_datetime(df['data_compra'], format='%d/%m/%Y')

file.close()