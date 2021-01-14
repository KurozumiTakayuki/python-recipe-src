import matplotlib.pyplot as plt
import numpy as np

# 対象データ
x = np.random.normal(0, 10, 1000)
# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, bins=10, color="#00AAFF", ec="#0000FF", alpha=0.5)

# 表示する
plt.show()
