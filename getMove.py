import string

def getMove():

    ## ask for input
    move = input("Your move: ")
    
    ## only take the first two chars
    move = move[:2]

    # no bad input handling yet

    ## 1st char is y value, convert ASCII to int value
    y = move[0]
    y = (ord(y) - 65) # subtract value of capital A to set to zero-origin for array index

    ## 2nd char is x value, cast to int
    x = move[1]
    x = (int(x) - 1) # subtract 1 to set to zero-origin for array index

    # print(str(x) + "," + str(y))

    return (x,y)
    