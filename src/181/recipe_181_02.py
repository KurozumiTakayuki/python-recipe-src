# 数値を倍にする関数
def calc_double(n):
    return n * 2


l1 = [1, 3, 6, 50, 5]

map1 = map(calc_double, l1)
for x in map1:
    print(x)

l2 = list(map1)
print(l2)
