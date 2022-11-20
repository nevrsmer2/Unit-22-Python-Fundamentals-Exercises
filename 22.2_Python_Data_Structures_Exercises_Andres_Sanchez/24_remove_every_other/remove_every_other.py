def remove_every_other(lst):
    """Uses slice() to remove every other element in the list  starting and index 0 to the end and return it in a new list without mutating list arg"""
    results = lst[::2]
    return results


# remove_every_other([1, 2, 3, 4, 5])

    # result = [lst[index] for index in range(1, len(list), 2)]
    # return result


    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
