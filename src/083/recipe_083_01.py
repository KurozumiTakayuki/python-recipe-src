def sample_generator():
    """ ジェネレータ関数 """
    print("処理開始")
    yield 'おはよう'
    print("処理再開")
    yield 'こんにちは'
    print("処理再開")
    yield 'こんばんば'


gen_obj = sample_generator()  # ジェネレータオブジェクトを生成する
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
