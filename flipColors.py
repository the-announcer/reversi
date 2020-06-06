def flipColors(b, pieces):
    
    for px in pieces:

        y = px[0]
        x = px[1]
        player = px[2]

        b[y][x] = player
    
    pieces = []
    return b