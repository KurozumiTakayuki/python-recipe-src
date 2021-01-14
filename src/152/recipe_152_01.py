# 中括弧単体
text = "こんにちは、{}さん。現在{}時です。"
name = "Suzuki"
time = 10

ftext = text.format(name, time)
print(ftext)

# フィールド番号
text = "こんにちは、{0}さん。現在{1}時です。"
name = "Suzuki"
time = 10

ftext = text.format(name, time)
print(ftext)


# フィールド名
text = "こんにちは、{name}さん。現在{time}時です。"
name = "Suzuki"
time = 10

ftext1 = text.format(name=name, time=time)
print(ftext1)
