from flipColors import flipColors
from validate import validate

def inspectBoard(move, b, heading, pieces) -> list:

    y = move[0]
    x = move[1]
    player = move[2]

    compass = {

        # visual of compass heading on grid
        # 0,1,2
        # 7,*,3
        # 6,5,4

        0: (y-1, x-1, player),
        1: (y-1, x, player),
        2: (y-1, x+1, player),
        3: (y, x+1, player),
        4: (y+1, x+1, player),
        5: (y+1, x, player),
        6: (y+1, x-1, player),
        7: (y, x-1, player)
    }

        
    if (heading is None):
        heading = range(len(b))
        for h in heading:

            target = compass[h]
            
            ## check for array out of bounds
            if validate(target, b):
                dst_sq = b[target[0]][target[1]]
            else:
                continue

            if (dst_sq == player):
                flipColors(b, pieces)
            elif (dst_sq == '-'):
                pieces = []
            else:
                pieces.append(target)
                inspectBoard(target, b, h, pieces)

    else:
        target = compass[heading]
        
        ## check for array out of bounds
        if validate(target, b):
            dst_sq = b[target[0]][target[1]]
        
        if (dst_sq == player):
            flipColors(b, pieces)
        elif (dst_sq == '-'):
            pieces = []
        else:
            pieces.append(target)
            inspectBoard(target, b, heading, pieces)
    
    return b
