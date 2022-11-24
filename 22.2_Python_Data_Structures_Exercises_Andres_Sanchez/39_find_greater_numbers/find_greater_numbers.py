def find_greater_numbers(nums):

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count




# Code I wrote.  Does not work on "find_greater_numbers([5, 4, 3, 2, 1])"
# def find_greater_numbers(nums):
#     count = 0
#     start = []

#     for n in range(0, len(nums)): 
#         start.append(nums[n])
#         # if start < n:
#         count += 1

#     # print('Start:', start)
#     print('Count:', count)


#         if nums[n] > nums[n-1]:
#             count += 1
#     print(count)

# [1, 2, 3]








    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """