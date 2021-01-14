import matplotlib.pyplot as plt

# 対象データ
label = ["A", "B", "C", "D", "E"]
x = [40, 30, 15, 10, 5]

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.pie(x, labels=label, counterclock=False, startangle=90)

# 表示補正
ax.axis('equal')

# 表示する
plt.show()
