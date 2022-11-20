def mode(lst):
    '''Converts the list into a dictionary and indicates how many times each key appears in list as the value.  It then sorts the dictionary based on the values, converts it to a list, and then returns the last element in the list, which is the number that appers most in the list arg'''
    num_count = {}
    for num in lst:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] = num_count[num] +1
    sorted_dict = list({k: v for k, v in sorted(num_count.items(), key=lambda item: item[1])})
    return sorted_dict[-1]


# def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """



