import hashlib

key = "abcdefg"
sha256 = hashlib.sha256(key.encode()).hexdigest()
print(sha256)
