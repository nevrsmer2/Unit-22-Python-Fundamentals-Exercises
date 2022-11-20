def friend_date(a, b):
    items_a = []
    items_b = []
    
    for item in a:
        if type(item) == list:
            for X in item:
                items_a.append(X)
        else:
            items_a.append(item)
    
    for item in b:
        if type(item) == list:
             for Z in item:
                  items_b.append(Z)
        else:
            items_b.append(item)

    in_common = set(items_a) & set(items_b)
    if len(in_common) != 0:
        return True
    else:
        return False


    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """