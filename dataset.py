import json
import pandas as pd

file = open('data/vendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

print(df['Data da Venda'])

file.close()