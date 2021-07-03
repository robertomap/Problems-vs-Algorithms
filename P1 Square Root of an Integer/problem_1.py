# Udacity Data Structures and Algorithms
# Project 3 - Problem #1 - Square Root

import math
import random

def mysqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Trivial Cases
    if number in [0, 1]:
        return number
    # Edge case: Integer square root of a negative number
    if number < 0:
        return None
    
    # First guess
    prev_num = number
    curr_num = number // 2

    while True:

        curr_square = curr_num ** 2

        # If too high try half the current value
        if curr_square > number:
            prev_num = curr_num
            curr_num = curr_num // 2
        
        # If too low try middle ground between previous and current values
        elif curr_square < number:

            # Limit condition for non exact square root.
            if curr_num == prev_num - 1:
                return curr_num
        
            curr_num = (prev_num - curr_num) // 2 + curr_num
        
        # If exact, return the current number
        else:
            return curr_num


print('\n# Test case 1: Some elementar numbers')
print(mysqrt(4), mysqrt(9), mysqrt(16), mysqrt(25), mysqrt(36), mysqrt(49))
# It is expected to see 2, 3, 4, 5, 6 and 7 as results

print('\n# Test case 2: Edge case: Square root of a negative number')
print(mysqrt(-1))
# It is expected to see ´None´ as result

print('\n# Test case 3: Edge case: Minimum operating arguments: Trivial cases')
print(mysqrt(0), mysqrt(1))
# It is expected to see 0 and 1 as results

print('\n# Test case 4: Edge case: 30-character integer')
for i in range(5):
    num = int(random.random()*10000000000000000000000000000000) 
    myresult = mysqrt(num)
    comparison = math.isqrt(num)
    if  myresult == comparison:
        print("{}) ´True´ for {}, mysqrt({}) == math.isqrt({})".format(i+1, num, myresult, comparison))

