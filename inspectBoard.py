from flipColors import flipColors

def inspectBoard(move, b, heading, pieces) -> tuple:

    y = move[0]
    x = move[1]
    player = move[2]

    compass = {

        # visual of compass on grid
        # 0,1,2
        # 3,M,5
        # 6,7,8

        0: (y-1, x-1, player),
        1: (y, x-1, player),
        2: (y+1, x-1, player),
        3: (y-1, x, player),
        4: (y, x, player), # self
        5: (y+1, x, player),
        6: (y-1, x+1, player),
        7: (y, x+1, player),
        8: (y+1, x+1, player)
    }

    ## we will check this direction on the board for an opposite player piece/move
    
    if heading == 4:
        for h in range(len(b)):
            target = compass[h]
           
            dst_y = target[0]
            dst_x = target[1]
            dst_sq = b[dst_y][dst_x]

            if (dst_sq == player):
                continue
            elif (dst_sq == '-'):
                continue
            else:
                target = (dst_y, dst_x, player)
                pieces.append(target)
                inspectBoard((dst_y, dst_x, player), b, h, pieces)

    else:
        target = compass[heading]

        dst_y = target[0]
        dst_x = target[1]
        dst_sq = b[dst_y][dst_x]

        if (dst_sq == player):
            # this is where we make the flips
            b = flipColors(b, pieces)
        elif (dst_sq == '-'):
            pass
        else:
            target = (dst_y, dst_x, dst_sq)
            pieces.append(target)
            inspectBoard((dst_y, dst_x, player), b, heading, pieces)

    return b
