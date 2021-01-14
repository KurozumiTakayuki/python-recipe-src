import math

l = [1, 64, 9, -49, 100]
for x in l:
    if x < 0:
        print(f"{x}はマイナスなので計算できません。スキップします。")
        continue
    s = math.sqrt(x)
    print(s)
