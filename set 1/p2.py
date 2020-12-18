#xor two hex

def xorfunc(a,b):
    boo = len(b)
    a = int(a, 16)
    b = int(b, 16)
    xor = hex(a ^ b)[2:].zfill(boo)
    return xor