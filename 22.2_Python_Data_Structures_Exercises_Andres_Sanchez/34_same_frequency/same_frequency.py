def same_frequency(num1, num2):
    num_1 = set(str(num1))
    num_2 = set(str(num2))
    if num_1 == num_2:
        return True
    else:
        return False





    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """