import os.path

path1 = r'suzuki\dir'
head1, tail1 = os.path.split(path1)
print(head1, tail1)

path2 = r'suzuki\dir' + '\\'
head2, tail2 = os.path.split(path2)
print(head2, tail2)

path3 = r'suzuki\dir\file.txt'
head3, tail3 = os.path.split(path3)
print(head3, tail3)
