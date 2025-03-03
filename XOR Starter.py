from pwn import *

# print(xor('label', 13))
value = 'label'
# convert to ascii
value = [chr(ord(i)^13) for i in value]

char = "".join(value)

print(char)
