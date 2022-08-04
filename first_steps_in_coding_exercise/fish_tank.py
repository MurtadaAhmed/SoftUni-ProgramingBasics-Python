length = int(input())
width = int(input())
height = int(input())
percent = float(input())
dimension = (length * width * height) / 1000
actual_dimension = dimension - (dimension * (percent/100))
print(actual_dimension)