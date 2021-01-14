import zipfile

with zipfile.ZipFile('sample.zip', 'r')as zf:
    print(zf.namelist())
