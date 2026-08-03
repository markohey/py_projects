def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")

    # Must be exactly 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    # Process first 9 characters (must be digits)
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)

    # Last character: digit or X
    if isbn[9] == 'X':
        total += 10
    elif isbn[9].isdigit():
        total += int(isbn[9])
    else:
        return False

    return total % 11 == 0
        
    
