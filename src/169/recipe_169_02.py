import random
import string

# ascii文字列で生成する場合
rtext1 = ''.join(random.choices(string.ascii_letters, k=5))
print(rtext1)

# asciiと数字で生成する場合
rtext2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
print(rtext2)
