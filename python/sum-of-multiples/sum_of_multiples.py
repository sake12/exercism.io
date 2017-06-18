def sum_of_multiples(number, multiplies):
    """
    Given a number, find the sum of all the multiples
    of particular numbers up to but not including that number.
    """
    return sum(i for i in range(number) if
               any(i % div == 0 for div in multiplies))