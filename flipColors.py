def flipColors(b, pieces):
    
    for px in pieces:

        x = px[0]
        y = px[1]
        p = px[2]

        b[x][y] = p
    
    return b