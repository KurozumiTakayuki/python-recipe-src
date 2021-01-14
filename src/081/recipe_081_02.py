def add_message(f):
    """ 関数の前後に開始・終了メッセージを追加する """

    def new_func(*args, **kwargs):
        print("処理を開始します")
        result = f(*args, **kwargs)
        print("処理を終了します")
        return result

    return new_func


# add_oneに対してデコレータで処理を追加
@add_message
def add_one(num):
    print("パラメータ:{}".format(num))
    return num + 1


# add_oneを実行
result = add_one(1)
print("戻り値:{}".format(result))
