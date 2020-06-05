def putMarker(marker, b, p):
    
    x = marker[0]
    y = marker[1]

    ## assuming move is legal for now
    # check to see if space is occupied
    if (b[x][y] != '-'):
        print('space occupied')
        return -1
    else:
        b[x][y] = p

    # print("putMarker: ", end="")
    # print(x, y, p)

    return b
    