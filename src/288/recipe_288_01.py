import matplotlib.pyplot as plt

# プロットする点
X = [1, 2, 3]
Y = [1, 1, 1]

# figureオブジェクトを生成する
fig = plt.figure()

# axesオブジェクトをfigureオブジェクトに設定する
ax = fig.add_subplot(1, 1, 1)

# axesオブジェクトに対して散布図を設定する
ax.scatter(X, Y, color='b', label='test_data')

# axesオブジェクトに対して凡例設定
ax.legend(["test1"])

# axesオブジェクトに対してタイトルを設定
ax.set_title("sample1")

# 表示する
plt.show()
