# Here we import string which contains all the alphabets
import string
# string function allows to access all the alphabets
Y=set(string.ascii_lowercase)
# Enter the user defined String value
user= input('please enter the string')
# compare the string function set values and user defined string
X=set(user)
# Print the result as True if the comparision matches
if X>=Y :
  print('true')
# Print the result as False if the comparision doesn't matches
else:
  print('false')