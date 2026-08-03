def square(number):
    
    if not isinstance(number, int) or (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
        
    return 2**(number-1)

def total():
    grand_tot = 0
    for i in range(1,65,1):
        grand_tot = grand_tot + square(i)
    return grand_tot
