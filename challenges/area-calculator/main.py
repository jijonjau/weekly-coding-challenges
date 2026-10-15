import math

shape = input("Enter the name of the shape you have in mind: ").strip().lower()

if shape == 'rectangle':
    length = int(input("Enter the length dimension: "))
    width = int(input("Enter the width dimension: "))
    area = length * width
    print(f"Area of {shape} of length {length} and width {width} is: {area:.2f}")
elif shape == 'triangle':
    base = int(input("Enter the base length: "))
    height = int(input("Enter the height: "))
    area = (base * height) / 2
    print(f"Area of {shape} of height {height} and base {base} is: {area:.2f}")
elif shape == 'circle':
    radius = int(input("Enter the radius: "))
    area = math.pi * math.pow(radius, 2) 
    print(f"Area of {shape} of radius {radius} is: {area:.2f}")
else:
    print("Shape should eiher be a rectangle, triangle or circle")