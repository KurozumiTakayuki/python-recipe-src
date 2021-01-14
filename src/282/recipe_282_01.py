import pandas as pd

data = {'height': [161, None, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data)
print(pd.isnull(df.height).any())
print(pd.isnull(df.weight).any())
