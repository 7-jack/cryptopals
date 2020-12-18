def xor_bytes(a, b):
    temporary_binary = ""
    for x, y in zip(a, b):
        print(x,y)
        print(str(bin(x[0])[2:]).zfill(8), str(bin(y[0])[2:]).zfill(8))
        temporary_binary += bin(x[0].zfill(8) ^ y[0].zfill(8))[2:].zfill(8)
    print(temporary_binary)
    return(temporary_binary)

def xor_string(a, b):
    asum = ""
    bsum = ""
    for letter in a:
        asum += bin(ord(letter))[2:].zfill(8)
    for letter in b:
        bsum += bin(ord(letter))[2:].zfill(8)

    return sum(bit1 != bit2 for bit1, bit2 in zip(asum, bsum))

print(xor_bytes([b'this is a test'], [b'wokka wokka!!!']))