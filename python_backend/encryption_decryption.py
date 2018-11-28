'''
cipher code
date: 11/15/2018
'''



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = list(alphabet)

def shift_letters(n):
    reverse = alphabet[::-1]
    return alphabet[n:] + reverse[len(alphabet) - n: len(alphabet) + 1]

print(shift_letters(-1))

def encrypt(text, n):
    text = text.upper()
    given_list = list(text)
    alphabet_list = list(alphabet)
    shifted_alphabet = list(shift_letters(n))
    new_text = []
    for i in given_list:
        if i == ' ':
            new_text += [' ']
        for x in alphabet_list:
            if i == x:
                new_text += [shifted_alphabet[alphabet_list.index(x)]]
    new_string = ''.join(new_text)
    return new_string

print(encrypt('attack at dawn', 1))

def decrypt(text, key):
    text = text.upper()
    given_list = list(text)
    alphabet_list = list(alphabet)
    shifted_alphabet = list(shift_letters(-key))
    new_text = []
    for i in given_list:
        if i == ' ':
            new_text += [' ']
        for x in alphabet_list:
            if i == x:
                new_text += [shifted_alphabet[alphabet_list.index(x)]]
    new_string = ''.join(new_text)
    return new_string

#print(decrypt('attack at dawn', 1))
