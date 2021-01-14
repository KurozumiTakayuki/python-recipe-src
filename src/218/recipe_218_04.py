import zipfile

with zipfile.ZipFile('sample.zip', 'r')as zf:
    zf.extractall(r'.\output', pwd=b'password')
