import tarfile

with tarfile.open('sample.tar.gz', 'r') as tar:
    tar.extractall(r'.\output')
