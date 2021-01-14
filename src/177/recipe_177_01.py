import re

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""

l1 = re.findall(r"^.*?$", text)
print(l1)

l2 = re.findall(r"^.*?$", text, flags=re.DOTALL)
print(l2)

l3 = re.findall(r"^.*?$", text, flags=re.DOTALL | re.MULTILINE)
print(l3)
