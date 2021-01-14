def outer_function():
    """ 外側の関数 """

    count = 0

    def inner_function():
        """ 内側の関数 """
        nonlocal count
        count += 1
        print("実行回数：{}回".format(count))

    return inner_function


# 関数オブジェクトを取得
func1 = outer_function()

# 関数を実行
func1()
func1()
func1()
