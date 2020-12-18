import secrets
import urllib.request
from Crypto.Cipher import AES
import base64
#assuming inputs is bytes for encrypt/decrypt functions

temp_bytes = base64.b64decode(urllib.request.urlopen("https://cryptopals.com/static/challenge-data/10.txt").read())
temp_key = b'YELLOW SUBMARINE'

def xor_byte_array(b1, b2):
    result = bytes(a ^ b for (a,b) in zip(b1,b2))
    return result


def random_AES_key():
    final_byte = secrets.token_bytes(16)
    return final_byte


def CBC_encrypt(plaintext, key, IV=bytes(16)):
    cipher = AES.new(key, AES.MODE_ECB)
    num_of_bytes = len(plaintext)
    byte_chunks_without_decryption = []  # splitting
    if num_of_bytes % 16 == 0:  # MUST GO BACK AND WORK ON PADDING FOR ALL
        for i in range(int(num_of_bytes / 16)):
            byte_chunks_without_decryption.append(bytes(plaintext[16 * i:16 * (i + 1)], "utf-8"))

        ciphertext = b""

        for i in range(len(byte_chunks_without_decryption)):
            if i == 0:
                new = cipher.encrypt(xor_byte_array(byte_chunks_without_decryption[i], IV))
                byte_chunks_without_decryption[i] = new
                ciphertext += new
            else:
                new = cipher.encrypt(xor_byte_array(byte_chunks_without_decryption[i], byte_chunks_without_decryption[i - 1]))
                byte_chunks_without_decryption[i] = new
                ciphertext += new
    return ciphertext



def ECB_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def CBC_decrypt(ciphertext, key, IV=bytes(16)):
    cipher = AES.new(key, AES.MODE_ECB)
    num_of_bytes = len(ciphertext)
    byte_chunks_without_decryption = [] #splitting
    if num_of_bytes % 16 == 0: #MUST GO BACK AND WORK ON PADDING FOR ALL
        for i in range(int(num_of_bytes/16)):
            byte_chunks_without_decryption.append(ciphertext[16*i:16*(i+1)])

        plaintext = ""
        
        for i in range(len(byte_chunks_without_decryption)):
            if i == 0:
                plaintext += (xor_byte_array(cipher.decrypt(byte_chunks_without_decryption[i]), IV)).decode('utf-8')
            else:
                plaintext += (xor_byte_array(cipher.decrypt(byte_chunks_without_decryption[i]), byte_chunks_without_decryption[i-1])).decode('utf-8')
    return plaintext


def ECB_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).decode("utf-8")
    return plaintext


print(CBC_decrypt(CBC_encrypt(CBC_decrypt(temp_bytes, temp_key), temp_key), temp_key))