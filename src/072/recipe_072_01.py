def func(x, y, **kwargs):
    print(f"引数x:{x}")
    print(f"引数y:{y}")
    if kwargs:
        print(f"3番目以降の引数:{kwargs}")


func(x=1, y=2)
print("-----")
func(x=1, y=2, z=3, w=4)
