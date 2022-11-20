def list_manipulation(lst, command, location, value=None):
    if command != 'add' and command != "remove":
        return None
    
    if location != 'beginning' and location != 'end':
        return None

    if type(value) != int:
        return None

# Add Element to Index [0]
    if command == 'add' and location == 'beginning':
        lst[0:0] = [value]
        return lst

# Remove Element from Index [-1]
    if command == 'add' and location == 'end':
        lst.extend([value])
        return lst

#Remove First Element
    if command == 'remove' and location == 'beginning':
        return lst.pop(0)

 #Remove Last Element
    if command == 'remove' and location == 'end':
        return lst.pop()

list_manipulation(lst, 'add', 'beginning', 20)

list_manipulation(lst, 'remove', 'beginning', 20)










    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
