from matplotlib import pyplot

# プロットする点
X = [1, 2, 3]
Y = [1, 1, 1]

# 関数を呼び出してプロット
pyplot.scatter(X, Y, c='b', label='test_data')

# 関数を呼び出して凡例設定
pyplot.legend(['test1'])

# 関数を呼び出してタイトルを設定
pyplot.title("sample1")

# 表示
pyplot.show()
