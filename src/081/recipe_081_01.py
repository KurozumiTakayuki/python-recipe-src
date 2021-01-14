def add_message(f):
    """ 関数の前後に開始・終了メッセージを追加する """

    def new_func():
        print("処理を開始します")
        f()
        print("処理を終了します")

    return new_func


def sample_func():
    """ 実行メッセージを表示するだけの関数 """
    print("sample_funcの処理を実行します")


# sample_funcに対して処理を追加した関数を得る
decorated_func = add_message(sample_func)

# 処理を追加した関数を実行する
decorated_func()
