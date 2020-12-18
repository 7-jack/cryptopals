#converts hex to base64

import codecs

def hextob64(hex):
    b64 = codecs.encode(codecs.decode(hex, "hex"), "base64").decode()
    return b64