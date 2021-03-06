#made for p6

import codecs
from urllib.request import urlopen

def xorfunc(a,b):
  z = len(b)
  a = int(a, 16)
  b = int(b, 16)
  xor = str(hex(a ^ b))[2:].zfill(z)
  return xor

weights = {'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.015861, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.033149, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.051576, 't': 0.0729357, 'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182}

#list of xors possible
def singlexor(a, b): #xors a single letter "a" against long string b
    full = ""
    length = len(b)
    for x in range(0,length//2):
        xor = xorfunc(a, b[x*2:x*2+2])
        full += xor
    return full

#scores the raw hex files by seeing if the conversion turns into a letter
def scorehex(a):
  score = 0
  for x in range(len(a)//2): #cuts everything into bytes - every 2 hex digits is a single character
    cut = a[x*2:x*2+2]
    char = str(codecs.decode(cut, "hex"))[2:][:-1].lower() #converts hex to ascii
    if char in weights.keys():
      score += (weights.get(char)) #scores
  return score

#scores each possibility

def doit(a): #takes hex string
  dictofposs = {}
  for key in range(0, 256): #xoring each possibility
    result = singlexor(hex(key),a)
    dictofposs[result] = key
  scores = {}
  score_to_hash = {}
  for moo in dictofposs:
    y = scorehex(moo)
    scores[y] = moo
    score_to_hash[y] = moo
  final = codecs.decode(scores[max(scores)], "hex")
  final = str(final, 'utf-8') #this is literally a line of code that would of saved me so much work...
  return (final, chr(dictofposs[score_to_hash[max(scores)]])) #don't even try...