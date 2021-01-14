import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]}
df = pd.DataFrame(data)

condition = [True, False, True, False]

new_condition = (df.index % 2 == 0)
print(new_condition)
