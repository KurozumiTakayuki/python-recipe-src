list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
d = {key: value for key, value in zip(list1, list2)}
print(d)
