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
    for z in decrypt_pool:
        if compare(z, list_words) >= 0:
            return compare(z, list_words)


print(decrypter('KHOOR WKHUH'))
