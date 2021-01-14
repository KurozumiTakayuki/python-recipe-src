l1 = ['bc', 'ac', 'bD', 'AB']
l2 = sorted(l1)
print(l2)

l2 = sorted(l1, key=str.lower)
print(l2)
