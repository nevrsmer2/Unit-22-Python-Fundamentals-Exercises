def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    step = 1
    numbers = range(start, stop + step)
    for num in numbers:
     print(num)

count_up(5, 7)        
