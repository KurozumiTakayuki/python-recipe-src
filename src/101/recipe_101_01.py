def sum_abs(x, y):
    """ 2数の絶対値の和を求める（バグあり） """
    val = abs(x) + y
    assert val >= 0, "計算結果がマイナスです"
    return val


val1 = sum_abs(-200, 100)
print(val1)
val2 = sum_abs(100, -200)
print(val2)
