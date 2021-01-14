import pandas as pd

name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

# height列を[]で取得する
height = df["height"]
print(height)

# weight列を.で取得する
weight = df.weight
print(weight)
