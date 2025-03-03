# Function to convert hex string to bytes
def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

# Function to XOR two byte strings
def xor_bytes(byte_str1, byte_str2):
    return bytes(a ^ b for a, b in zip(byte_str1, byte_str2))

# Given hex values
KEY1 = hex_to_bytes("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_XOR_KEY1 = hex_to_bytes("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_XOR_KEY3 = hex_to_bytes("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_XOR_KEYS = hex_to_bytes("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Step 1: XOR the intermediate results to obtain the flag
# FLAG = (FLAG ⊕ KEY1 ⊕ KEY3 ⊕ KEY2) ⊕ KEY1 ⊕ KEY3 ⊕ KEY2
# Apply XOR operations based on the properties of XOR

# First XOR KEY2 ^ KEY1 and KEY2 ^ KEY3 to get KEY2 and KEY3
KEY2 = xor_bytes(KEY2_XOR_KEY1, KEY1)
KEY3 = xor_bytes(KEY2_XOR_KEY3, KEY2)

# Now, XOR the result with FLAG ⊕ KEY1 ⊕ KEY3 ⊕ KEY2 to obtain the FLAG
flag = xor_bytes(FLAG_XOR_KEYS, KEY1)
flag = xor_bytes(flag, KEY3)
flag = xor_bytes(flag, KEY2)

# Convert the flag from bytes to a readable hex string or ASCII (if needed)
print("Recovered flag:", flag.hex())  # In hexadecimal format
print("Recovered flag:", flag.decode())  # In ASCII