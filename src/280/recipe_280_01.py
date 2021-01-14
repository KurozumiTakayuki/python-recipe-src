import pandas as pd

name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# at
sato_weight = df.at['Sato', 'weight']
print(sato_weight)

# iat
tanaka_height = df.iat[3, 1]
print(tanaka_height)
