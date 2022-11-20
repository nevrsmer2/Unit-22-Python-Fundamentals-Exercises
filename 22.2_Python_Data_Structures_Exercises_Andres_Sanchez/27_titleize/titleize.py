def titleize(phrase):
    split_phrase =  phrase.split()
    first_caps = [word.capitalize() for word in split_phrase]
    new_str = ' '.join(first_caps)
    return new_str

#Or, all the above steps combined
    # result = ' '.join(word.capitalize() for word in phrase.split())
    # return result

#or:
#    return  str.title(phrase)


    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
