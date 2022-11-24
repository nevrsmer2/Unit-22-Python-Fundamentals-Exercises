def extract_full_names(people):
    # return [f"{person['first']} {person['last']}" for person in people]

    full_names = []

    for person in people:
            full_names.append(f"{person['first']} {person['last']}")
    return full_names


#     or:

# def extract_full_names(people):
#     return [f"{person['first']} {person['last']}" for person in people]




        # print([f"{person['first']} {person['last']}"])






# extract_full_names(names)



    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

