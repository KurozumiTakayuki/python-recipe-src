import re

text = "Beautiful is better than ugly."
replaced = re.sub(r"\s", "_", text)
print(replaced)
