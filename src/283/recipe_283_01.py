import pandas as pd

data = {'name': ['Apple', 'Oranggg', 'Banana'], 'price': [110, 120, 130]}
df = pd.DataFrame(data)
df2 = df.replace('Oranggg', 'Orange')
print(df2)
