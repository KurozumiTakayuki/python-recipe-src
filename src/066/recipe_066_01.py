import math

l = [1, 64, 9, -49, 100]
for x in l:
    if x < 0:
        print(f"{x}はマイナスなので計算できません。ループを抜けます")
        break
    s = math.sqrt(x)
    print(s)
