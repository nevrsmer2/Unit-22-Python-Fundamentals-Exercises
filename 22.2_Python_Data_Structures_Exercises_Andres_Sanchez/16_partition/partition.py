def partition(list, fn):
    are_str = []
    not_str = []

    if fn == "is_string":
        for word in list:
             if type(word) == str:
                 are_str.append(word)
             else:
                 not_str.append(word)
        return [are_str, not_str]

# partition(["hi", None, 6, "bye"], 'is_string')

    evens = []
    odds = []

    if fn == "is_even":
        for num in list:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
    return [evens, odds]

# partition([1, 2, 3, 4], 'is_even')


    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """