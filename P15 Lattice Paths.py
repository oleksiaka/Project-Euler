from math import factorial

x = 20
y = 20
paths = (factorial(x + y)) / (factorial(y) * factorial((x + y) - y))

print(paths)
