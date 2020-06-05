from flipColors import flipColors

def inspectBoard(marker, b, heading, pieces) -> tuple:

    x = marker[0]
    y = marker[1]
    p = marker[2]
    
    compass = {

        # visual of compass on grid
        # 1,2,3
        # 4,M,6
        # 7,8,9

        0: (x-1, y-1, p),
        1: (x, y-1, p),
        2: (x+1, y-1, p),
        3: (x-1, y, p),
        4: (x, y, p), # self
        5: (x+1, y, p),
        6: (x-1, y+1, p),
        7: (x, y+1, p),
        8: (x+1, y+1, p)
    }

    ## we will check this direction on the board for an opposite player piece/marker
    
    if heading == 4:
        for h in range(len(b)):
            target = compass[h]
           
            dst_x = target[0]
            dst_y = target[1]
            dst_p = b[x][y]

            if (dst_p == p):
                continue
            elif (dst_p == '-'):
                continue
            else:
                target = (dst_x, dst_y, dst_p)
                pieces.append(target)
                inspectBoard((dst_x, dst_y, p), b, h, pieces)

    else:
        target = compass[heading]

        dst_x = target[0]
        dst_y = target[1]
        dst_p = b[x][y]

        if (dst_p == p):
            # this is where we make the flips
            pass
        elif (dst_p == '-'):
            # set the pieces array to blank (discard them)
            pieces = []            
        else:
            target = (dst_x, dst_y, dst_p)
            pieces.append(target)
            inspectBoard((dst_x, dst_y, p), b, heading, pieces)

    
    b = flipColors(b, pieces)

    return b
