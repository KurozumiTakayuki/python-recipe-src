def func(x, y, z, a, b):
    print(x, y, z, a, b)
    return x + y + z + a + b


params1 = [1, 2, 3]
params2 = {"a": 4, "b": 5}
w = func(*params1, **params2)
print(w)
