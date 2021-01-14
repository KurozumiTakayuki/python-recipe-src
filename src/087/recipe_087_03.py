class Sample():
    class_val1 = 1
    class_val2 = 2

    def __init__(self):
        pass


Sample.class_val2 = 999

s = Sample()

# クラス変数が参照できる
print(s.class_val1, s.class_val2)

# 代入しようとする
s.class_val1 = 100

# 新たにインスタンス変数class_val1が設定される
print(s.class_val1, Sample.class_val1)
