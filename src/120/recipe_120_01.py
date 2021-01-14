with open("tmp.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    print(str(i) + ":" + line, end="")
