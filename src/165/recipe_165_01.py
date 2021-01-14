text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.


Explicit is better than implicit.

"""
lines = text.split("\n")
line_list = [line for line in lines if line.strip() != ""]
new_text = "\n".join(line_list)
print(new_text)
