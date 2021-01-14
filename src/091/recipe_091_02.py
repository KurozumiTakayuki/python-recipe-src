class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Sample(1, 2)
print(hasattr(s, 'x'))
print(hasattr(s, 'z'))

