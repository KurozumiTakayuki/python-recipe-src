s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

# s1 - s2
# s1 - s2 = s1にあってs2にないもの = A, B
s = s1.difference(s2)
print(s)

# s2 - s1
# s2 - s1 = s2にあってs1にないもの = D, E
s = s2.difference(s1)
print(s)
