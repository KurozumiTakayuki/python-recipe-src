import matplotlib.pyplot as plt
 
# ラベル
label = ['A', 'B', 'C', 'D', 'E']

# 対象データ
x = [1, 2, 3, 4, 5]  # 横軸
height = [3, 5, 1, 2, 3]  # 値

# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに棒グラフを設定する
ax.bar(x, height, label=label, linewidth=1, edgecolor="#000000")
# 表示する
plt.show()
