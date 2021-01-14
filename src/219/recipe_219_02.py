import zipfile

with zipfile.ZipFile('sample.zip', 'a')as zf:
    zf.write('tmp4.txt')
