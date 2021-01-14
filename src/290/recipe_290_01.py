import matplotlib.pyplot as plt

# figureを生成
fig1 = plt.figure()

# グラフ描画設定
ax = fig1.add_subplot(1, 1, 1)
x1 = [-2, 0, 2]
y1 = [-2, 0, 2]
ax.plot(x1, y1)

x2 = [-2, 0, 2]
y2 = [-4, 0, 4]
ax.plot(x2, y2)

ax.grid(True)  # grid表示ON
ax.set_xlim(left=-2, right=2)  # x範囲
ax.set_ylim(bottom=-2, top=2)  # y範囲
ax.set_xlabel('x')  # x軸ラベル
ax.set_ylabel('y')  # y軸ラベル
ax.set_title('ax title')  # グラフタイトル
ax.legend(['f(x)=x', 'g(x)=2x'])  # 凡例を表示
plt.show()
