from inspectBoard import inspectBoard

def flipColors(marker, b, search_direction):
    
    # x = marker[0]
    # y = marker[1]
    # p = marker[2]

    next_marker = inspectBoard(marker, b, search_direction)

    # print(next_marker)