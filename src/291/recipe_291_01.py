from matplotlib import pyplot as plt
import numpy as np

# ランダムな点を生成する
x = np.random.rand(50)
y = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# プロットマーカーの大きさ、色、透明度を変更
ax.scatter(x, y, s=300, alpha=0.5, linewidths=2, marker='*', c='#aaaaFF', edgecolors='blue')
plt.show()
