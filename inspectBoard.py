def inspectBoard(marker, b, heading) -> tuple:

    pieces = []

    x = marker[0]
    y = marker[1]
    p = marker[2]

    compass = {

        # visual of compass on grid
        # 1,2,3
        # 4,M,6
        # 7,8,9

        1: (x-1, y-1, p),
        2: (x, y-1, p),
        3: (x+1, y-1, p),
        4: (x-1, y, p),
        5: (x, y, p), # self
        6: (x+1, y, p),
        7: (x-1, y+1, p),
        8: (x, y+1, p),
        9: (x+1, y+1, p)
    }

    ## we will check this direction on the board for an opposite player piece/marker
    
    if heading == 5:
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
                inspectBoard((dst_x, dst_y, p), b, h)

    else:
        target = compass[heading]
        # lots more to do in this direction since we found a possible set of pieces to replace


    return target
