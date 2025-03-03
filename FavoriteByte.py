value = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

value = bytes.fromhex(value)

for i in range(0, 256):
    pri = [v ^ i for v in value]

    char = "".join([chr(i) for i in pri])
    print(char + " " + str(i))