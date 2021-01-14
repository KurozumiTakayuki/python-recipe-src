def outer_function():
    """ 外側の関数 """

    def inner_function():
        """ 内側の関数 """
        print('inner_functionが実行されました')

    # 内側の関数を変数として返す
    return inner_function


func = outer_function()
func()
