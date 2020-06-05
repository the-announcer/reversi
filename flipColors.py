from inspectBoard import inspectBoard

def flipColors(marker, b, heading):
    
    x = marker[0]
    y = marker[1]
    p = marker[2]

    if (b[x][y] == p):
        return -1
    elif (b[x][y] == '-'):
        return -2
            

    