import math

num1String = input('Please enter an integer: ')
num1 = int(num1String)
area = math.pi * num1 * num1
circumference = 2 * math.pi * num1
print(area, circumference)
