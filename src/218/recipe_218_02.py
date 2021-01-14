import zipfile

with zipfile.ZipFile('sample.zip', 'r')as zf:
    zf.extract('tmp.txt', r'.\output')
