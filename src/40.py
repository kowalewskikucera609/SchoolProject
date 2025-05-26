import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Parameters:
    - length: int, desired length of the generated string
    
    Returns:
    - str, randomly generated string with uniform length
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

if __name__ == "__main__":
    print("Random String:", generate_random_string(10))
