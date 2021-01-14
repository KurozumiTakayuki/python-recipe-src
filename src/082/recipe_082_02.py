fruits_list = ["バナナ", "リンゴ", "みかん"]
for fruit in map(lambda x: "★" + str(x) + "★", fruits_list):
    print(fruit)
