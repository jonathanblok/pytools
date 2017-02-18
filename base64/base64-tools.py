import base64

encoded = base64.b64encode('Blabla')
data = base64.b64decode(encoded)
print(data)
