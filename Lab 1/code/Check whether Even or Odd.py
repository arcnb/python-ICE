# collect a integer value from the user
n = int(input('Please enter an integer: '))
# enter the loop only if user gives non-zero integer
if n !=0:
    # given integer value is divided by 2
    r = n % 2
    # print the result as EVEN number if the remainder is zero
    if r == 0:
        print("Given number is EVEN")
    # print the result as ODD number if the remainder is non-zero
    else:
        print("Given number is ODD")
