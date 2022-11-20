def list_check(lst):
    for element in lst:
        if type(element) != list:
            return False
    else:
        return True

        





    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False

        list_check([1, ["nope"]])
    """
