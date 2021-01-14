import pandas as pd

name = ["Yamada", "Suzuki", "Sato", "Tanaka", "Watanabe"]
score1 = {'kokugo': [55, 81, 73, 63, 88], 'sansu': [95, 80, 99, 79, 77]}
score2 = {'kokugo': [65, 74, 75, 59, 58], 'sansu': [97, 69, 72, 83, 66]}
df1 = pd.DataFrame(score1, index=name)
df2 = pd.DataFrame(score2, index=name)

sum_df = df1 + df2
print(sum_df)
