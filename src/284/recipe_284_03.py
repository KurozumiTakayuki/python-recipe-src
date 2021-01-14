import pandas as pd

data = {'Food': ["Apple cake", "Orange juice", "Apple pie", "Strawberry cake"], 'score': [80, 72, 90, 78]}
df = pd.DataFrame(data)

condition = df.Food.str.contains('Apple.*')
print(df[condition])
