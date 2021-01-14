import matplotlib.pyplot as plt

# 1. figureを生成する
fig = plt.figure()

# 2. 生成したfigureにaxesを生成、配置する
ax1 = fig.add_subplot(1, 1, 1)

# 3. axesに描画データを設定する
X = [0, 1, 2]
Y = [0, 1, 2]
ax1.plot(X, Y)

# 4. 表示する
plt.show()
