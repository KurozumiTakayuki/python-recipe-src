d1 = {"key1": 100, "key2": 200}
d2 = {"key2": 220, "key3": 300, "key4": 400}
d3 = dict(d1, **d2)
print(d3)
