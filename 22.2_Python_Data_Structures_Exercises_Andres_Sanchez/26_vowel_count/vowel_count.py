from executing import only

def vowel_count(phrase):
    phrase_lower = phrase.lower()
    vowels = 'aeiouAEIOU'
    only_vowels = ""
    vowel_count = {}

    for letter in phrase_lower:
        if letter in vowels:
            only_vowels+= letter

    for ltr in only_vowels:
        if ltr not in vowel_count:
            vowel_count[ltr] =1
        else:
            vowel_count[ltr] = vowel_count[ltr] +1
    return vowel_count



    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """