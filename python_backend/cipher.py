'''
cipher code
date: 11/15/2018
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class encrypt_code:

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def shift_letters(n):
        reverse = alphabet[::-1]
        return alphabet[n:] + reverse[len(alphabet) - n: len(alphabet) + 1]

    def key()

    def encrypt(given, shift_cipher):

        for i in given
