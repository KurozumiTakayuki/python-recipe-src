count = 0


def func():
    global count
    count += 1
    print("実行回数：{}回".format(count))


func()
func()
print("countの値：{}".format(count))
