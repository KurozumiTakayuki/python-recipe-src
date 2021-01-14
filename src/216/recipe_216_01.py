import codecs

u_text = "\u307f\u304b\u3093"
text = codecs.decode(u_text.encode())
print(text)
