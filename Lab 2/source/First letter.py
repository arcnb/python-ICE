# To print a pattern, we use matrix variables
for a in range(7):
    # A row matrix with a range of 7 elements is taken
    for b in range(5):
        # A column matrix with a range of 5 elements is taken
        if ((b == 0) or (a == 0) or (a == 3) or (b == 4) and (b > 0)):
            # To print the letter A, above condition in the matrix should be true
            print('*', end='')
            # prints the resultant positions with '*' wherever the above condition is true
        else:
            print(end=' ')
            # resultant answers should be empty, if the value is false
    print()
