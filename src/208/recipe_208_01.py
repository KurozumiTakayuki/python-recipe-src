import base64

with open("python-powered-h-50x65.png", 'br') as f:
    bin_img = f.read()
    b64_img = base64.b64encode(bin_img).decode()
    print(b64_img)
