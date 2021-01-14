import matplotlib.pyplot as plt

# figureを生成する
fig = plt.figure()

# 2x3の1番目
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title('1')  # グラフタイトル
# 2x3の2番目
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_title('2')  # グラフタイトル
# 2x3の3番目
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_title('3')  # グラフタイトル
# 2x3の4番目
ax4 = fig.add_subplot(2, 3, 4)
ax4.set_title('4')  # グラフタイトル
# 2x3の5番目
ax5 = fig.add_subplot(2, 3, 5)
ax5.set_title('5')  # グラフタイトル
# 2x3の6番目
ax6 = fig.add_subplot(2, 3, 6)
ax6.set_title('6')  # グラフタイトル

# 表示する
plt.show()
