import numpy as np

# 基底(1, 1, 0)、(0, -1, 0)
a = np.array([[1, 1], [1, -1], [0, 0]])

# QR分解
q, r = np.linalg.qr(a)
print(q)
print(r)
