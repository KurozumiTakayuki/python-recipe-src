import re

text = "Errors should never pass silently."
m_obj = re.search(r"p...", text)
print(m_obj.group())
print(m_obj.start())
print(m_obj.end())
