def fibonacci_generator():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


fib_gen = fibonacci_generator()

# 10項目まで取り出す
for i in range(0, 10):
    num = next(fib_gen)
    print(num)
