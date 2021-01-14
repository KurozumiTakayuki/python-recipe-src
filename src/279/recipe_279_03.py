import pandas as pd

name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
data = {'height': [161, 168, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data, index=name)

mod_yamada =  pd.Series([171, 66], index=["height", "weight"])
df.loc["Yamada"] = mod_yamada
print(df)
