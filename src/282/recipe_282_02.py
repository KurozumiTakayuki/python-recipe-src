import pandas as pd

data = {'height': [161, None, 173, 169, 188], 'weight': [55, 63, 78, 59, 68]}
df = pd.DataFrame(data)

height_series = df.height

# heightの列を取得し、欠損値を除去する
new_height_series = height_series.dropna()
print(new_height_series)

# DataFrameの欠損値がある行を除去する
new_df = df.dropna()
print(new_df)
