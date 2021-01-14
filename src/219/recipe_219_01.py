import zipfile

with zipfile.ZipFile('sample.zip', 'w')as zf:
    zf.write('tmp1.txt')
    zf.write('tmp2.txt')
    zf.write('tmp3.txt')
