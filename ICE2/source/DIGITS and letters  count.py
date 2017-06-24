string = input("Input a string")
digit=0
letter=0
for c in string:
    if c.isdigit():
        digit= digit+1
    elif c.isalpha():
        letter= letter+1
    else:
        pass
print("Letters", letter)
print("Digits", digit)
