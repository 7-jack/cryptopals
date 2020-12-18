import urllib.request
from Crypto.Cipher import AES
import base64


page = urllib.request.urlopen("https://cryptopals.com/static/challenge-data/7.txt")
contents = base64.b64decode(page.read())

key = "YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)

final = cipher.decrypt(contents).decode("utf-8")

print(final)