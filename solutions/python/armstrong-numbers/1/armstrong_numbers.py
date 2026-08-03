def is_armstrong_number(number):
    num_str = str(number)
    num_dig = len(num_str)

    tot = 0
    for i in num_str:
        tot = tot + int(i)**int(num_dig)

    return number == tot
