def putMarker(move, b, player):
    
    x = move[0]
    y = move[1]

    ## assuming move is legal for now
    # check to see if space is occupied
    if (b[x][y] != '-'):
        print('space occupied')
        return -1
    else:
        b[x][y] = player

    # print("putMarker: ", end="")
    # print(x, y, p)

    return b
    