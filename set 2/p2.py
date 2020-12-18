import urllib.request
from Crypto.Cipher import AES
import base64
import codecs

#cbc decryptor

def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

page = base64.b64decode(urllib.request.urlopen("https://cryptopals.com/static/challenge-data/10.txt").read())
blocks = []
for i in range(int(len(page)/16)):
    blocks.append(page[16*i:16+16*i])

list = ""

iv = bytes([0 for i in range(16)])

def decrypt(content):
    decrypted_message = ""

    key = b"YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)

    for i in range(180):
        if i == 0:
            final = cipher.decrypt(blocks[i])    #.decode("utf-8")
            message = byte_xor(final, iv)
            decrypted_message += str(message)[2:-1]
        else:
            final = cipher.decrypt(blocks[i])
            message = byte_xor(final, blocks[i-1])
            decrypted_message += str(message)[2:-1]
    #encoded = base64.b64encode(final)

    return decrypted_message


x = [i for i in decrypt(page).split("\\n")]
for boo in x:
    print(boo)