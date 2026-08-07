def is_paired(input_string):
    
    brack_list = []
    open_brack = ["[", "{", "("]
    closed_brack = ["]", "}", ")"]
    
    for char in input_string:
        if char in open_brack:
            brack_list.append(char)
        elif char in closed_brack:
            if len(brack_list) == 0:
                return False
            elif open_brack.index(brack_list[-1]) == closed_brack.index(char):
                brack_list.pop()
            else:
                return False

    if len(brack_list) == 0:
        return True
    return False