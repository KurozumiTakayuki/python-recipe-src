import pandas as pd

name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)
print(df)

# locでindex="Sato"のデータを取得する
sato = df.loc["Sato"]
print(sato)

# ilocでindex=3のデータを取得する
tanaka = df.iloc[3]
print(tanaka)
