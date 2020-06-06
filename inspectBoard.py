from flipColors import flipColors

def inspectBoard(move, b, heading) -> tuple:

    x = move[0]
    y = move[1]
    player = move[2]

    compass = {

        # visual of compass on grid
        # 1,2,3
        # 4,M,6
        # 7,8,9

        0: (x-1, y-1, player),
        1: (x, y-1, player),
        2: (x+1, y-1, player),
        3: (x-1, y, player),
        4: (x, y, player), # self
        5: (x+1, y, player),
        6: (x-1, y+1, player),
        7: (x, y+1, player),
        8: (x+1, y+1, player)
    }

    ## we will check this direction on the board for an opposite player piece/move
    
    if heading == 4:
        for h in range(len(b)):
            target = compass[h]
           
            dst_x = target[0]
            dst_y = target[1]
            dst_player = b[x][y]

            if (dst_player == player):
                continue
            elif (dst_player == '-'):
                continue
            else:
                target = (dst_x, dst_y, dst_player)                
                pieces.append(target)
                inspectBoard((dst_x, dst_y, player), b, h)

    else:
        target = compass[heading]

        dst_x = target[0]
        dst_y = target[1]
        dst_player = b[x][y]

        if (dst_player == player):
            # this is where we make the flips
            pass
        elif (dst_player == '-'):
            # set the pieces array to blank (discard them)
            pieces = []            
        else:
            target = (dst_x, dst_y, dst_player)
            pieces.append(target)
            inspectBoard((dst_x, dst_y, player), b, heading)

    
    b = flipColors(b, pieces)

    return b
