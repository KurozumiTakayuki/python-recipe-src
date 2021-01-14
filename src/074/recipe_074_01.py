def func(x, y, z):
    print(x, y, z)
    return x + y + z


params = {"x": 1, "y": 2, "z": 3}
w = func(**params)
print(w)
