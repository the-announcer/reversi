
def validate(target, b):

    dst_y = target[0]
    dst_x = target[1]

    if (dst_y < 0) or (dst_y >= len(b)):
        return False
    elif (dst_x < 0) or (dst_x >= len(b)):
        return False

    return True