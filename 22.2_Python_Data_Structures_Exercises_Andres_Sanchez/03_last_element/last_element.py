def last_element(lst):
    if lst == []:
        return None
    return lst[-1]
    
    # or:
    # return lst[-1:]

    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """