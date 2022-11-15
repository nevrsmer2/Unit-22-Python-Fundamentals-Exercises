def is_palindrome(phrase):
    str = phrase.replace(' ','').lower()
    str_reversed = str[::-1]

    if str == str_reversed:
        return True
    else:
        return False

    '''Determines if the phrase is a palindrome by comparing the phrase passed in  that is set to a variable to the same phrase  that is reveresed and set to another  varriable '''


    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
