def multiply_even_numbers(nums):
    evens = []
    total = 0
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    if len(evens) == 1:
        return evens[0]
    if len(evens) == 0:
        return 1
    for num in evens:
        total += num * evens[+1]
    return total







    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """