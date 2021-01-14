import numbers


def calc10times(num):
    if not isinstance(num, numbers.Number):
        raise TypeError('パラメータが不正です')

    return num * 10


val = calc10times(10)
print(val)
val = calc10times('abc')
print(val)
