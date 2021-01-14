import pandas as pd
import numpy as np

school = ["A", "A", "A", "A", "B", "B", "B", "B", "B"]
grade = [1, 2, 2, 1, 2, 1, 1, 2, 2]
height = [161, 178, 173, 169, 188, 179, 170, 169, 171]
weight = [55, 63, 78, 59, 68, 59, 65, 55, 77]
data = {'school': school, 'grade': grade, 'height': height, 'weight': weight}
df = pd.DataFrame(data)

df2 = df.pivot_table(index=['school'], columns=['grade'], values='height', fill_value=0, aggfunc=np.average)
print(df2)
