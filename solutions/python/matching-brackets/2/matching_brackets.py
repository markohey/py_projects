def is_paired(input_string):
    """
        Function receives a series of string characters, then determines if string series contains brackets which matches or not.
        :input_string: string
    """
    
    brack_list = []
    open_brack = ["[", "{", "("]
    closed_brack = ["]", "}", ")"]
    
    for char in input_string:
        if char in open_brack:
            brack_list.append(char)
        elif char in closed_brack:
            if len(brack_list) == 0:
                return False
            if open_brack.index(brack_list[-1]) == closed_brack.index(char):
                brack_list.pop()
            else:
                return False

    if len(brack_list) == 0:
        return True
    return False