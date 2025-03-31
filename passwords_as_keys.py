from Crypto.Cipher import AES
import hashlib

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    # key = bytes.fromhex(password_hash)

    cipher = AES.new(password_hash, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

# print(words)
for i in words:
    KEY = hashlib.md5(i.encode()).digest()
    val = bytes.fromhex(decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", KEY).get('plaintext'))
    try:
        decoded_data = val.decode('utf-8')
        print("Decoded text:", decoded_data)
    except UnicodeDecodeError:
        pass
        # print("decode error")
