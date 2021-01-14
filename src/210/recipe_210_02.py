import uuid

u3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
print(str(u3))
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(str(u5))
