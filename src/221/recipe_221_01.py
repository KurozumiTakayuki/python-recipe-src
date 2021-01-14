import tarfile

with tarfile.open("sample.tar.gz", "w:gz") as tar:
    tar.add("tmp1.txt")
    tar.add("tmp2.txt")
