def func(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


print("---第1引数のみ指定した結果---")
func(1)

print("---可変長引数を指定した結果---")
func(1, 100, 200, 300, a="X", b="Y", c="Z")
