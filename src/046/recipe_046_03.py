d = {"key1": 100, "key2": 200}
# 存在するキーを指定
val1 = d.get("key1")
print(val1)

# 存在しないキーを指定
val2 = d.get("keyX")
print(val2)

# 上のコードの続き
val3 = d.get("keyX", 999)
print(val3)
