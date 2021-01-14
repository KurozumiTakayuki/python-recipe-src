import chardet

with open("tmp.txt", mode='rb') as f:
    result = chardet.detect(f.read())
    print(result)
