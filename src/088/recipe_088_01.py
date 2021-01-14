class Sample():
    class_val1 = 1

    def __init__(self, val1):
        self.instance_val1 = val1

    def instance_method(self):
        print(self.class_val1, self.instance_val1)

    @classmethod
    def class_method(cls):
        print(cls.class_val1)

    @staticmethod
    def static_method():
        local_val = 100
        print(local_val)


# インスタンスメソッドの呼び出し
s = Sample(10)
s.instance_method()
# クラスメソッドの呼び出し
Sample.class_method()
# スタティックメソッドの呼び出し
Sample.static_method()
