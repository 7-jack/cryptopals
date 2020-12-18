#decrypt repeating key xor
import base64
import statistics
import p4alternative
from urllib.request import urlopen
import codecs


def ham_string(a, b):
    asum = ""
    bsum = ""
    for letter in a:
        asum += bin(ord(letter))[2:].zfill(8)
    for letter in b:
        bsum += bin(ord(letter))[2:].zfill(8)

    return sum(bit1 != bit2 for bit1, bit2 in zip(asum, bsum))

#thank god for ham_bytes...
def ham_bytes(a, b):
    temporary_binary = ""
    for x, y in zip(a, b):
        temporary_binary += bin(x[0] ^ y[0])[2:].zfill(8)
    return(temporary_binary.count('1'))


def possible_keysizes(list_of_bytes):
    keysize_scores = {} #store keys and their ham distances
    #decoded_bytes = base64.b64decode(base64bytes) #decode b64 to bytes
    #list_of_bytes = [bytes([i]) for i in decoded_bytes] #make bytes from string to list
    for keysize in range(2,42):
        hamming_distances = [] #stores distances for each keysize
        counter = 0
        while counter+2*keysize <= len(list_of_bytes):
        #for i in range(2):
            ham_dist = ham_bytes(list_of_bytes[counter:counter + keysize], list_of_bytes[counter + keysize:counter + 2 * keysize]) #
            hamming_distances.append(ham_dist)
            #print(list_of_bytes[counter:counter+keysize], list_of_bytes[counter+keysize:counter+2*keysize])
            counter += keysize
            #print(ham_dist)
        try:
            keysize_scores[keysize] = statistics.mean(hamming_distances)/keysize
        except:
            pass
    final = sorted(keysize_scores, key=keysize_scores.get)
    #return(keysize_scores)
    return(final)


def transpose_blocks(keysize, list_of_bytes):
    counter = 0
    list_of_blocks = []
    while keysize+counter <= len(list_of_bytes):
        list_of_blocks.append(list_of_bytes[counter:counter + keysize])
        counter += keysize
    list_of_transposed_characters = []
    for i in range(keysize):
        temp_list = [moo[i] for moo in list_of_blocks]
        list_of_transposed_characters.append(temp_list)
    return list_of_transposed_characters


def score_transposition(list_of_transposed_characters):
    decodedchars = []
    keychars = []
    for block in list_of_transposed_characters:
        hexstring = [byteblock.hex() for byteblock in block] #convert the hex bytes to hex string
        hexstring = ''.join(hexstring)
        decodedchar, keychar = p4alternative.doit(hexstring)
        decodedchars.append(decodedchar)
        keychars.append(keychar)
    return decodedchars, keychars


def determine_final_string(decodedchars, keylength):
    final_string = ''
    for i in range(keylength):
        temp = [str[i] for str in decodedchars]
        temp = ''.join(temp)
        final_string += temp
    return final_string


def determine_final_key(keychars):
    keychars = ''.join(keychars)
    return keychars


def given_ciphertext(ciphertext):
    decoded_bytes = base64.b64decode(ciphertext)
    list_of_bytes = [bytes([i]) for i in decoded_bytes] #make bytes from string to list
    top5_keysizes = possible_keysizes(list_of_bytes)[0:5]
    message_and_key = {}
    for i in top5_keysizes:
        list_of_transposed_characters = transpose_blocks(i, list_of_bytes)
        decodedchars, keychars = score_transposition(list_of_transposed_characters)
        x = determine_final_string(decodedchars, i)
        y = determine_final_key(keychars)
        message_and_key[x] = y
    message_and_score = {} #could be much easier way... but i've spent too long on this so just gonna do this instead
    for thing in message_and_key:
        a = codecs.encode(bytes(thing, 'utf-8'), 'hex')
        message_and_score[thing] = p4alternative.scorehex(a)
    boop = max(message_and_score, key=message_and_score.get)
    x = boop
    y = message_and_key[boop]

    return x, y


data = urlopen("https://cryptopals.com/static/challenge-data/6.txt").read()
contents = data.decode("utf-8")
x = contents.split()
x, y = given_ciphertext(''.join(x))
print('\n\n/// the decrypted code is ///', 3*'\n'), print(x), print(3*'\n'), print('/// the key is ///\n'), print(y, '\n'), print(':)')