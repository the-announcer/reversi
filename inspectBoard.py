def inspectBoard(marker, b, heading) -> tuple:

    x = marker[0]
    y = marker[1]
    p = marker[2]

    compass = {
        '1': (x-1, y-1, p),
        '2': (x, y-1, p),
        '3': (x+1, y-1, p),
        '4': (x-1, y, p),
        '6': (x+1, y, p),
        '7': (x-1, y+1, p),
        '8': (x, y+1, p),
        '9': (x+1, y+1, p)
    }

    ## we will check this direction on the board for an opposite player piece/marker
    target = compass[heading]
            
    dst_x = target[0]
    dst_y = target[1]
    dst_p = b[x][y]

    return (dst_x, dst_y, dst_p)
