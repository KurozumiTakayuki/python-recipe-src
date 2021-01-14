import numpy as np

a = np.array([[1, 3], [2, -1]])

# 行列表示
print(a)

# 転置
print(a.T)

# トレース
print(a.trace())

# 逆行列
print(np.linalg.inv(a))

# 行列式
print(np.linalg.det(a))

# ランク
print(np.linalg.matrix_rank(a))
