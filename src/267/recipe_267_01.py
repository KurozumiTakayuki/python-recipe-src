import numpy as np

a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
w, v = np.linalg.eig(a)

# 固有値
print(w)

# 固有ベクトル
print(v)
