import numpy as np

# 係数行列
coef = np.array([[3, 1], [1, 3]])

# 定数の行列
dep = np.array([9, 0])

# 連立方程式の解
ans = np.linalg.solve(coef, dep)

# 解を出力
print(ans)

# 検算
c1 = 3 * ans[0] + 1 * ans[1]
c2 = 1 * ans[0] + 3 * ans[1]
print(c1, c2)
