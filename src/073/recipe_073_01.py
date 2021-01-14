def func(x, y, z):
    print(x, y, z)
    return x + y + z


params = [1, 2, 3]
w = func(*params)
print(w)
