def putMarker(marker, b):
    
    x = marker[0]
    y = marker[1]

    ## assuming move is legal for now
    # check to see if space is occupied
    if (b[x][y] != '-'):
        print('space occupied')
        return -1

      
    