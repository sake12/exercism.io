from itertools import compress


class Allergies(object):
    """
    Given a person's allergy score, determine whether or not they're allergic
    to a given item, and their full list of allergies.
    """

    def __init__(self, number):
        allergies = ['eggs',
                     'peanuts',
                     'shellfish',
                     'strawberries',
                     'tomatoes',
                     'chocolate',
                     'pollen',
                     'cats']

        # convert int to binary, then to list of digits, then reverse list
        binary = [int(i) for i in bin(number)[2:]][::-1]
        # and use compress()
        self.lst = list(compress(allergies, binary))

    def is_allergic_to(self, allergy):
        """Find if list of allergies contains given allergen. """
        return allergy in self.lst
