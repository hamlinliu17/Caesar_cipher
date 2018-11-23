'''
cipher code
date: 11/15/2018
'''



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = list(alphabet)

def shift_letters(n):
    reverse = alphabet[::-1]
    return alphabet[n:] + reverse[len(alphabet) - n: len(alphabet) + 1]


def encrypt(text, n):
    text = text.upper()
    given_list = list(text)
    alphabet_list = list(alphabet)
    new_text = []
    for i in given_list:
        if i == ' ':
            new_text += [' ']
        for x in alphabet_list:
            if i == x:
                new_text += [alphabet_list[alphabet_list.index(x) + n]]
    new_string = ''.join(new_text)
    return new_string

print(encrypt('hello', 1))

def decrypt(text, key):
    text = text.upper()
    given_list = list(text)
    alphabet_list = list(shift_letters(key))
    new_text = []
    for i in given_list:
        if i == ' ':
            new_text += [' ']
        for x in alphabet_list:
            if i == x:
                new_text += [alphabet_list[alphabet_list.index(x) - key]]
    new_string = ''.join(new_text)
    return new_string
