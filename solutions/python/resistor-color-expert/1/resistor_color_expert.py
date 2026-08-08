def resistor_label(colors):
    resist_sum = ""
    c_vals = {"black": "0",
                 "brown": "1",
                 "red": "2",
                 "orange": "3",
                 "yellow": "4",
                 "green": "5",
                 "blue": "6",
                 "violet": "7",
                 "grey": "8",
                 "white": "9"}
    
    c_tols = {"grey": "±0.05%",
             "violet": "±0.1%",
             "blue": "±0.25%",
             "green": "±0.5%",
             "brown": "±1%",
             "red": "±2%",
             "gold": "±5%",
             "silver": "±10%"}

    if len(colors) == 1:
        return "{} ohms".format(c_vals[colors[0]])
        
    for color in colors[:len(colors)-2]:
        resist_sum += c_vals[color]
    resist_sum = int(resist_sum)*10**int(c_vals[colors[len(colors)-2]])

    result = ""
    if resist_sum >= 1_000_000_000:
        result = str(resist_sum / 1_000_000_000) + " gigaohms"
    elif resist_sum >= 1_000_000:
        result = str(resist_sum / 1_000_000) + " megaohms"
    elif resist_sum >= 1_000 and resist_sum % 1_000 == 0:
        result = str(int(resist_sum / 1_000)) + " kiloohms"
    elif resist_sum >= 1_000:
        result = str(resist_sum / 1_000) + " kiloohms"
    else:
        result = str(resist_sum) + " ohms"
        
    return "{} {}".format(result, c_tols[colors[-1]])
    