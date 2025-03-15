import random
from math import sqrt

def random_code():
    # Function to generate a random Python code
    code = f"""
# This is a simple school project for my classmates and me to collaborate on.
# We're going to use this project to learn about Python!

# First, let's import the random module
import random

# Next, we'll define a function that takes in two numbers and returns their sum
def add(a, b):
    return a + b

# Now, let's use the random module to generate two random numbers
random_number1 = random.randint(1, 10)
random_number2 = random.randint(1, 10)

# And now, we'll add them together using our function
result = add(random_number1, random_number2)

# Finally, let's print the result
print(f"The sum of {random_number1} and {random_number2} is {result}")
"""
    return code