def includes(collection, sought, start=None):

# For Sets if Start Index Ignorede
    if type(collection) == set:
        return sought in collection

# For Sets  if Start Index Not Ignored
    # if type(collection) == set and type(start) == int:
    #     new_list = list(collection)
    #     list_slice = new_list[start:]
    #     return sought in list_slice

# For Dictionaries
    if collection == dict:
        values =[ val for val in collection.values()]
        return sought in values

# For Strings, Lists, and Tuples
    else:
        tuple_slice = collection[start:]
        return sought in tuple_slice




# In [106]: ages = [5, 9, 10, 22, 44, 9, 10, 33, 82]

# In [107]: new_ages = list(ages[3:])

# In [108]: new_ages
# Out[108]: [22, 44, 9, 10, 33, 82]

# In [109]: 9 in new_ages
# Out[109]: True
    




    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """