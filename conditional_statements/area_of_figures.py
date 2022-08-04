from math import pi
type_figure = input()
result = 0
if type_figure == "square":
    side = float(input())
    result = side * side
elif type_figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif type_figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif type_figure == "triangle":
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f"{result:.3f}")