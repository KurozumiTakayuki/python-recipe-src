def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(split_list(l, 3))
print(result)
