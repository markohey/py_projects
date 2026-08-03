def value(colors):
    """Calculates the total resistance of a resistor based on a pre-specified color code.
    """
    # create function to easily refer to color list
    def color_list():
        return ["black",
               "brown",
               "red",
               "orange",
               "yellow",
               "green",
               "blue",
               "violet",
               "grey",
               "white"]

    
    color_num = [str(color_list().index(color)) for color in colors[:2]]
    res = ''.join(color_num)
    return int(res)