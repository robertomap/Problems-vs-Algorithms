# Udacity Data Structures and Algorithms
# Project 3 - Problem #6 - Unsorted Integer Array

import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # Edge Cases: Invalid input argument
    if type(ints) != list or ints == []:
        return None

    min = ints[0]
    max = ints[0]
    
    for val in ints:
    
        # Edge Cases: Invalid input entry
        if type(val) != int:
            return None
        
        # Min and Max checks
        if val < min:
            min = val
        elif val > max:
            max = val
    
    return (min, max)


# Test Cases

print('\nTest Case 1: Problem statement example - Test Case of Ten Integers')
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# It is expected to pass the test.



print('\nTest Case 2: Some random list')
lst = [i for i in range(0, random.randint(1, 50))]  # a of a random size
random.shuffle(lst)
print(lst)
print ("Pass" if ((min(lst), max(lst)) == get_min_max(lst)) else "Fail")
# It is expected to pass the test.

 

print("\nTest Case 3: Edge Case - Empty list")
lst = []
print(get_min_max(lst))
# It is expected to return an None object.



print("\nTest Case 4: Edge Case - Invalid entries")
lst = [1, 3, 2, 6, 5, '4', 7]
print(get_min_max(lst))
# It is expected to return an None object.



print("\nTest Case 5: Edge Case - Invalid argument type")
lst = 12345
print(get_min_max(lst))
# It is expected to return an None object.
