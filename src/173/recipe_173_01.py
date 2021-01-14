import re

text = "Special cases aren't special enough to break the rules."
splited = re.split(r"[^a-zA-Z0-9]+", text)
print(splited)
