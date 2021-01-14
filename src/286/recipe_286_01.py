import pandas as pd

grade = [1, 2, 1, 3, 2, 3]
height = [161, 168, 173, 169, 188, 169]
weight = [55, 63, 78, 59, 68, 59]
data = {'grade': grade, 'height': height, 'weight': weight}
df = pd.DataFrame(data)

df2 = df.sort_values(['grade', 'weight', 'height'], ascending=[True, False, False])
print(df2)
