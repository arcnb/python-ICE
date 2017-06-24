#Defining horizontal function
def print_horiz_line():
    # print as first row element
    print("    ",end='  ')
    #  end=' ' actually means that you want a space after the end of the statement ("    ") instead of a new line character.
    print("--- " * X)

#Defining vertical function
def print_vert_line():
    # print as first coloumn element
    print("    ", end=' ')
    print("|   " * (X+1))


if __name__ == "__main__":
    X = int(input("size of game board is "))

    for box in range(X):
        print_horiz_line()

        print_vert_line()

    print_horiz_line()