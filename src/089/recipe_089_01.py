class Sample():
    def __init__(self, val1):
        self.__instance_val1 = val1

    def __private_method(self):
        print(self.__instance_val1)


s = Sample(10)
print(s.__instance_val1)
