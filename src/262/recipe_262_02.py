import numpy as np

x = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(x[0, 2])  # 1行3列の13が取得できる
print(x[2, 0])  # 3行1列の31が取得できる
