import base64

string = "Roger"
print('Plain Text String: '+string)

b64str = string

for i in range(15):
    b64str = base64.b64encode(b64str)
    print('Base64 Encoded String ' + str(i+1) + ': ' + b64str[:70])