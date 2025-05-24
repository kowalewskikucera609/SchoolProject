import random

def play_dice():
    numbers = [1, 2, 3, 4, 5, 6]
    roll = random.choice(numbers)
    print(f"You rolled a {roll}.")
