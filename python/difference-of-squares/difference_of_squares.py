def square_of_sum(number):
    return ((1 + number) * (number / 2))**2


def sum_of_squares(number):
    return number**3 / 3 + number**2 / 2 + number / 6


def difference(number):
    """The difference between the square of the sum and the sum of the squares of the first N natural numbers."""
    return square_of_sum(number) - sum_of_squares(number)
