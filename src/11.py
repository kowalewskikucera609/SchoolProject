import random

def get_random_code():
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(8):
        code += random.choice(numbers)
        code += random.choice(letters)
    return code