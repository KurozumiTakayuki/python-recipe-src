def func(x, y, *args):
    print(f"1番目の引数:{x}")
    print(f"2番目の引数:{y}")
    if args:
        print(f"3番目以降の引数:{args}")


func(1, 2)
print("-----")
func(1, 2, 3, 4, 5)
