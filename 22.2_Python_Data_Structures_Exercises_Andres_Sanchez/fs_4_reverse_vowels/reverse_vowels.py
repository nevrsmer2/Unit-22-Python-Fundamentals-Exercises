def reverse_vowels(s):

def reverse_vowels(s):

    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)



# Sources:
#     1. https://stackoverflow.com/questions/66688611/reverse-only-vowels-in-a-string

#     2. https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-71.php

#     3. https://www.geeksforgeeks.org/reverse-vowels-given-string/

    
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """