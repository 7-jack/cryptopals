#freqanalysis of hex xor two digit

import p2

possibles = []
weights = {'E': 13, 'T': 12, 'A': 11, 'O': 10, 'I': 9, 'N': 8, ' ': 7, 'S': 6, 'H': 5, 'R': 4, 'D': 3, 'L': 2, 'U': 1}

listposs = []

def singlexor(a, b):
    full = ""
    length = len(b)
    for x in range(0,length//2):
        xor = p2.xorfunc(a, b[x*2:x*2+1])
        full += xor
    return full

print(singlexor("EE", "ED"))