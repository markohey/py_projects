def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Raise error is number is not a positive integer
    if not isinstance(number, int) or number <= 0:
         raise ValueError("Classification is only possible for positive integers.")

    # Determine factors of number and add to list if modulus == 0
    fac = [i for i in range(1, number) if number % i == 0]
    """fac = []
    for i in range(1,number):
        if number % i == 0:
            fac.append(i)"""

    # Determine if number is perfect, abundant or deficient
    al_sum = sum(fac)
    if al_sum == number:
        return "perfect"
    elif al_sum > number:
        return "abundant"
    else:
        return "deficient"
