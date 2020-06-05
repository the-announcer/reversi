from translateDirection import translateDirection

def flipColors(marker, b, search_direction):
    
    x = marker[0]
    y = marker[1]

    next_marker = translateDirection(marker, search_direction)