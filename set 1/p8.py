import urllib.request
from Crypto.Cipher import AES
import collections
import codecs

page = urllib.request.urlopen("https://cryptopals.com/static/challenge-data/8.txt")
contents = page.read().split(b'\n')
ciphertexts = [line for line in contents]
decrypted = []

#decrypts against test key
for ciphertext in ciphertexts:
    key = "ABCDEFGHIJKLMNOP"
    cipher = AES.new(key, AES.MODE_ECB)
    final = cipher.decrypt(ciphertext)
    decrypted.append(final)

#groups a single line into chunks
def chunkinto16(a):
    chunks = []
    count = 0
    while count + 16 < len(a):
        chunk = a[count:count+16]
        chunks.append(chunk)
        count += 16
    return chunks

#score one group of chunks from a single line
def scorechunk(chunk):
    pos = 0
    score = 0
    allposbytes = []
    while pos < 16:
        slicebytes = []
        for x in chunk:
            slicebytes.append(x[pos])
        counter = collections.Counter(slicebytes).values()
        for value in counter:
            if value > 1:
                score += value
        pos += 1
        allposbytes.append(slicebytes)
    return(score)

scores = {}
lines_made_into_chunks = []

for line in decrypted:
    lines_made_into_chunks.append(chunkinto16(line))

line_number = 0
for line in lines_made_into_chunks:
    score = scorechunk(line)
    scores[line_number] = score
    line_number += 1

line, score = max(scores, key=scores.get) + 1, max(scores.values())

print("The line most likely using AES-ECB encryption is line number", line)