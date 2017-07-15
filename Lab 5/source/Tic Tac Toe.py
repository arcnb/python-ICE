GB=[(['.']* 4) for i in range(4)]
R=[0]
t = 1
#verify valid input
def input_valid(val):
    if len(val)!=2:
        return 0
    try:
        if(1<= int(val[0]) <= 4) and (1<= int(val[0]) <= 4):
            if GB[int(val[0]) - 1][int(val[1]) - 1] != '.':
                return 0
            return 1
        else:

            return 0
    except ValueError:

        return 0
def DB(val,player):
    GB[int(val[0]) - 1][int(val[1])- 1] = player
    for R in GB:
        print(R)
def GO():
    T = 1
    seht='.'

    # verify row winning
    for i in range(3):
        if len(set(GB[i])) == 1:
            if GB[i][1] == '.':
                continue
            elif GB[i][1] == 'X':
                print ("game finished - Player1 win's")

            else:
                print ("game finished - Player2 win's")
            return 1

    # verify coloumn winning
    for i in range(3):
        if GB[0][i] == GB[1][i] == GB[2][i]:
            if GB[0][i] == '.':
                continue
            elif GB[0][i] == 'X':
                print ("game finished - Player1 win's")
            else:
                print ("game finished - Player2 win's")
            return 1

    # verify daiognal winning
    if (GB[0][0] == GB[1][1] == GB[2][2]) or (GB[0][2] == GB[1][1] == GB[2][0]):
        if GB[1][1] == 'X':
            print ("game finished - Player1 win's")
        elif GB[1][1] == 'O':
            print ("game finished - Player2 win'ss")
        else:
            return 0
        return 1
    for sublist in GB:
        if seht in sublist:
            return 0
    return 1
while not GO():
    dot = '.'

    while not input_valid(R):
        player = t %2
        if player == 0:
            player = 2
            dot = 'O'
        else:
            dot = 'X'
        play1 = input('Player ' + str(player) + ' input: ')
        R = play1.split(",")
    DB(R, dot)
    R = [0]
    t += 1