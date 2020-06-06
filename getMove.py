import string

def getMove(p):

    ## ask for input
    move = input("Your move, {}: ".format(p))
    
    ## only take the first two chars
    move = move[:2]

    # no bad input handling yet

    ## 1st char is x value, convert ASCII to int value
    x = move[0].upper()
    x = (ord(x) - 65) # subtract value of capital A to set to zero-origin for array index

    ## 2nd char is y value, cast to int
    y = move[1]
    y = (int(y) - 1) # subtract 1 to set to zero-origin for array index

    # print(str(x) + "," + str(y))

    # board array location reference is reverse from user input
    return (y,x,p)
    