#Give the input values in a newline seperated by comma
mylist =input("enter input:\n")
#convert the comma seperated input into list
X=mylist.split(",")
#sorting the elements in a list using SORTED key word
output = sorted(X)
#Using .join() to display comma seperated elements in the above sorted list
print (','.join(output))