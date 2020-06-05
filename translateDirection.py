def translateDirection(marker, search_direction) -> tuple:
    
    x = marker[0]
    y = marker[1]

    search_direction = search_direction.lower()


    directions = {
        'nw': (x-1, y-1),
        'n': (x, y-1),
        'ne': (x+1, y-1),
        'w': (x-1, y),
        'e': (x+1, y),
        'sw': (x-1, y+1),
        's': (x, y+1),
        'se': (x+1, y+1)
    }

    next_marker = directions[search_direction]

    return(next_marker)