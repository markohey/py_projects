def convert(number):
    mess = ""
    
    if number % 3 == 0:
        mess += "Pling"
        
    if number % 5 == 0:
        mess += "Plang"
        
    if number % 7 == 0:
        mess += "Plong"

    if (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
        mess = str(number)
        
    return mess