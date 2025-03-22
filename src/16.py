def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers))
