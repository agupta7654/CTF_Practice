from Cryptodome.Util.number import *

num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
message = long_to_bytes(num).decode()  # Convert to bytes and decode to string
print(message)  