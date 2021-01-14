import math
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
size = math.ceil(len(l1) / n)
l2 = [l1[idx:idx + size] for idx in range(0, len(l1), size)]
print(l2)
