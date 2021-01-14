# 数値を倍にする関数
def calc_double(n):
    return n * 2


l1 = [1, 3, 6, 50, 5]

# map関数を使用してl1の要素を全て倍にしてmap1に格納
map1 = map(calc_double, l1)

# map型をlist型に変換したものをl2に格納
l2 = list(map1)

print(l2)
