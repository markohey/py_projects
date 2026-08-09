def commands(binary_str):
    actions = ["jump", "close your eyes", "double blink", "wink"]
    result = []
    
    for i, digit in enumerate(binary_str[1:]):
        if digit == "1":
            result.append(actions[i])

    if binary_str[0] == "0":
        result.reverse()    

    return result
