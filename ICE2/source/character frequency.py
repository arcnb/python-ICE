charstr = input("Enter the string: ")
dict = {}
for char in charstr:
    value = charstr.count(char)
    dict[char] = value
print("frequency of the string:\n{} - {}".format(charstr,dict))