import re

text = "Errors should never pass silently."
m_obj = re.search(r"(n....)\s(p...)", text)
print(m_obj.group())
print(m_obj.groups())

