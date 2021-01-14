import matplotlib.pyplot as plt
import numpy as np

# 対象データ
x = np.linspace(0, 5, 100)  # x軸の値
y1 = x ** 2
y2 = np.sin(x)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, "-")
ax.plot(x, y2, "-")

# 表示する
plt.show()
