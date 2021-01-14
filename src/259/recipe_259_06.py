import numpy as np

# 配列を生成(dtypeの指定なし)
x1 = np.array([1, 2, 3])
print(x1.dtype)

# 配列を生成(dtypeにfloat64を指定)
x2 = np.array([1, 2, 3], dtype=np.float64)
print(x2.dtype)