import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02     紅茶（お徳用A）
203 TE02     紅茶（お徳用B）"""

items = re.findall(r'([0-9]+) +([0-9A-Z]+) +(.*)', text)
print(items)
