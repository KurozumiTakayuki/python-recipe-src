import mojimoji

text = "ｐｙｔｈｏｎ パイソン １０００"
print(mojimoji.zen_to_han(text))
print(mojimoji.zen_to_han(text, kana=False))
print(mojimoji.zen_to_han(text, digit=False))
print(mojimoji.zen_to_han(text, ascii=False))
