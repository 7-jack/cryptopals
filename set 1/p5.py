#encrypts?
key = "ICE"
message = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

count = 0
full = ""
for letter in message:
  x = (hex(ord(letter) ^ ord(key[count % 3]))[2:].zfill(2))
  full += (hex(ord(letter) ^ ord(key[count % 3]))[2:].zfill(2))
  count += 1
print(full)