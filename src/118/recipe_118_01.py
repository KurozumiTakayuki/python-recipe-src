# 比較演算子

x = 0
y = 1
z = 2

if x < y < z:
    print("適正範囲内です")

# 複数の判定
name = "火薬"
if name in ("燃料", "火薬"):
    print("輸送できません")

# Trueの判定
flg = True
if flg:
    print("フラグがONです")

# 三項演算子
x = 200 if flg else 100

# ループ
data = (1, 2, 3, 4,)
for val in data:
    print(val)

# 同時代入
text1 = text2 = text3 = "init value"

# リスト内包表記
l1 = [7, 11, 2, 5, 10, 3]
l2 = [val * 2 for val in l1]

# 不適切な変数名
# sum = x + y NG例：以降sum関数が使用できなくなる
sum_val = x + y

# 変数の入れ替え
x, y = y, x
