import base64

value = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
intermediate = bytes.fromhex(value)
print(base64.b64encode(intermediate).decode('utf-8'))