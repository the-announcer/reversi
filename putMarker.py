def putMarker(move, b, player):
    
    y = move[0]
    x = move[1]

    ## assuming move is legal for now
    # check to see if space is occupied
    if (b[y][x] != '-'):
        print('space occupied')
        return -1
    else:
        b[y][x] = player

    return b
    