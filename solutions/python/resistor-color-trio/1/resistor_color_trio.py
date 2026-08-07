def label(colors):
    sum = ""
    color_code = {"black": "0",
             "brown": "1",
             "red": "2",
             "orange": "3",
             "yellow": "4",
             "green": "5",
             "blue": "6",
             "violet": "7",
             "grey": "8",
             "white": "9"}

    for color in colors[:2]:
        sum += color_code[color]

    sum = int(sum)*10**int(color_code[colors[2]])

    if sum == 0:
        return "0 ohms"
    elif sum % 1_000_000_000 == 0:
        return str(int(sum/1_000_000_000)) + " gigaohms"
    elif sum % 1_000_000 == 0:
        return str(int(sum/1_000_000)) + " megaohms"    
    elif sum % 1_000 == 0:
        return str(int(sum/1_000)) + " kiloohms"
    else:
        return str(sum) + " ohms"