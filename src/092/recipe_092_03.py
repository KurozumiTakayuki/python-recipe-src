class Sample1():
    """ スーパークラス """
    pass


class Sample2(Sample1):
    """ Sample1のサブクラス """
    pass


obj1 = Sample1()  # Sample1型のオブジェクトを生成する
obj2 = Sample2()  # Sample2型のオブジェクトを生成する

print(" ----- isinstanceによる比較結果 ----- ")
print(isinstance(obj1, Sample1))  # True
print(isinstance(obj1, Sample2))  # False
print(isinstance(obj2, Sample1))  # True
print(isinstance(obj2, Sample2))  # True

print(" ----- Typeの結果比較 ----- ")
print(type(obj1) == Sample1)  # True
print(type(obj1) == Sample2)  # False
print(type(obj2) == Sample1)  # False
print(type(obj2) == Sample2)  # True
