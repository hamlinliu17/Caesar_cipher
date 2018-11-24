from encryption_decryption import *
from list_of_words import *

'''
a decrypter function that takes encrypted text and outputs the key number

utilizes a list of 1000 english words ()
'''

def decrypter(text):
    list_encrypt = text.split()
    decrypt_pool = []
    for i in range (1, 27):
        decrypt_pool += [decrypt(list_encrypt[0], i)]
    for i in decrypt_pool:
        index_num = decrypt_pool.index(i)
        i = i.lower()
        if compare(i, list_words) >= 0:
            return index_num + 1


k = encrypt('attack at dawn', 8)
print(decrypt(k, decrypter(k)))
