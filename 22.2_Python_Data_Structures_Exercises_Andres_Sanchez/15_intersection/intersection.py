def intersection(list_1, list_2):
    '''Converts list arguments into sets, intersects the sets, and then converts the intersected set to a list'''
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    inter_list = list(set_1.intersection(set_2))
    return inter_list



    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    [1,2,3].intersection([2,3,4])

    [1,2,3] & [2,3,4]