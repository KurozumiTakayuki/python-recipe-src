class Sample():
    class_val1 = 1
    class_val2 = 2

    def __init__(self):
        pass


Sample.class_val2 = 999
print(Sample.class_val1, Sample.class_val2)
