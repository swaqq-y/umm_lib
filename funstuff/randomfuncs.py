import random

def flipcoin():
    return random.choice(["Heads", "Tails"])
def custom_flipcoin(variant1, variant2):
    if isinstance(variant1, str) and isinstance(variant2, str):
        return random.choice(variant1, variant2)
    else:
        return "All two options must be in str format."
def rolldice():
    return random.randint(1, 6)