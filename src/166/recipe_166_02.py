import mojimoji

text = "python ﾊﾟｲｿﾝ 1000"
print(mojimoji.han_to_zen(text))
print(mojimoji.han_to_zen(text, kana=False))
print(mojimoji.han_to_zen(text, digit=False))
print(mojimoji.han_to_zen(text, ascii=False))
