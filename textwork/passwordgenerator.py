import random

def password_gen(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[/   ]^_`{|}~'
    result = ''
    for i in range(length):
        result += characters[random.randint(len(characters))]
    return result
def onlyletters_gen_password(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[/   ]^_`{|}~'
    result = ''
    for i in range(length):
        result += characters[random.randint(len(characters))]
    return result
