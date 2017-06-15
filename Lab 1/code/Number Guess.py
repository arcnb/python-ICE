# To Generate integer from 0 to 9 import random package
import random
# randint function picks random digit from 0 to 9
program = random.randint(0, 9)
print("A random digit is generated by the program in [0,9]")
# collect the user guessed integer value
guess = int(input('Guess the random digit from 0 to 9: '))
# check whether user guess digit is higher, lower or equal to the random value generated by the program
if program > guess:
    # print the result if guess value is lower than random value
    print("Your guess is LOWER than required")
elif program == guess:
    # print the result if guess value equals random value
    print("Your guess is perfect")
else:
    # print the result if guess value is higher than random value
    print("Your guess is HIGHER than required")
# print the random value generated by the program
print("Random digit via program is ", program)
