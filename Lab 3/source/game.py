GB=[(['.']* 4) for i in range(4)]
R=[0]
t = 1

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