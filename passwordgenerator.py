import random

def password_gen(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result = ''
    for i in range(length):
        result += characters[random.randint(len(characters))]
    return result