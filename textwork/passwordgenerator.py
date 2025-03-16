import random

def passwordgen(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[/   ]^_`{|}~'
    result = ''
    for i in range(length):
        result += characters[random.randint(len(characters))]
    return result
def letter_passwordgen(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += characters[random.randint(len(characters))]
    return result
