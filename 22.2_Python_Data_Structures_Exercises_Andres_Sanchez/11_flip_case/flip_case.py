def flip_case(phrase, letter):

    for ltr in phrase:
        if ltr == letter:
            return phrase.replace(ltr, ltr.swapcase())

# * * Does not work.  Only flips the case of the letter passed in


"""Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
