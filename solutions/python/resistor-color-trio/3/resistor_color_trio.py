def label(colors):
    csum = ""
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
        csum += color_code[color]

    csum = int(csum)*10**int(color_code[colors[2]])

    if csum == 0:
        return "0 ohms"
    if csum % 1_000_000_000 == 0:
        return str(int(csum/1_000_000_000)) + " gigaohms"
    if csum % 1_000_000 == 0:
        return str(int(csum/1_000_000)) + " megaohms"    
    if csum % 1_000 == 0:
        return str(int(csum/1_000)) + " kiloohms"
    return str(csum) + " ohms"