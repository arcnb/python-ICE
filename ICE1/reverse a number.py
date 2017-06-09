num1String = input('Please enter an integer: ')
num1 = int(num1String)
reverse = 0

while num1 != 0:
    r = num1 % 10
    num1 = num1 // 10
    reverse = reverse * 10 + r
print("reverse",reverse)
