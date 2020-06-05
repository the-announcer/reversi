def inspectBoard(marker, b, heading) -> tuple:


    heading = heading.lower()
    
    x = marker[0]
    y = marker[1]
    p = marker[2]

    compass = {
        'nw': (x-1, y-1, p),
        'n': (x, y-1, p),
        'ne': (x+1, y-1, p),
        'w': (x-1, y, p),
        'e': (x+1, y, p),
        'sw': (x-1, y+1, p),
        's': (x, y+1, p),
        'se': (x+1, y+1, p)
    }

    target = compass[heading]
            
    dst_x = target[0]
    dst_y = target[1]
    dst_p = b[x][y]

    return (dst_x, dst_y, dst_p)
