import random

def flipcoin():
    return random.choice(["Heads", "Tails"])
def custom_flipcoin(variant1, variant2):
    if isinstance(variant1, str) and isinstance(variant2, str):
        return random.choice([variant1, variant2])
    else:
        return "All two options must be in str format."
def rolldice():
    return random.randint(1, 6)
def custom_rolldice(variant1, variant2, variant3, variant4, variant5, variant6):
    return random.choice([variant1, variant2, variant3, variant4, variant5, variant6])
def rock_paper_scissors(variant):
    res = ''
    chos = random.choice(["rock", "paper", "scissors"])
    if variant.lower() == "rock" and chos == "scissors":
        res = 'Win!!'
    elif variant.lower() == "paper" and chos == "rock":
        res = 'Win!!'
    elif variant.lower() == "scissors" and chos == "paper":
        res = "Win!!"
    elif variant.lower == chos:
        res = "Drawn game!"
    elif variant.lower() == "paper" and chos == "scissors":
        res = 'Lose:('
    elif variant.lower() == "rock" and chos == "paper":
        res = 'Lose:('
    elif variant.lower() == "scissors" and chos == "rock":
        res = 'Lose:('
    return res
