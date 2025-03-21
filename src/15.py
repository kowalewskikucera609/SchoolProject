def calculate_area(shape):
    if shape == "circle":
        radius = 10
        area = 3.14 * radius ** 2
    elif shape == "rectangle":
        length = 20
        width = 5
        area = length * width
    else:
        print("Unsupported shape")
        return

    print(f"The area of {shape} is {area}")

calculate_area("circle")
calculate_area("rectangle")
