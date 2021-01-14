from sys import argv

if 3 <= len(argv):
    print(argv[0])
    print(argv[1])
    print(argv[2])
else:
    print("引数を3つ指定してください。")
