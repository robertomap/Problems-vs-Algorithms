# Udacity Data Structures and Algorithms
# Project 3 - Problem #2 - Search in a Rotated Sorted Array

import random

def find_pivot_point(start, end, input_list):
    """
    Uses binary search to find the index of the lowest value 
    in a rotated sorted array (ascending).
    Args:
       start(int), end(int): indexes for a search interval
       input_list(array): Input array to search
    Returns:
       int: index of the lowest value
    """

    # Stop condition: Unordered vector part of size 2 means the 
    # last element is the minimum one
    if (end - start) <= 1:
        return end

    # The segment (start through end) is divided in two parts by a middle index
    middle = (end - start) // 2 + start

    # If last element of this part is less than the first one, it means this 
    # part is unordered and the pivot point is here
    if input_list[middle] < input_list[start]:
        return find_pivot_point(start, middle, input_list)

    # Although, if this part is unordered, then the pivot point is here
    elif input_list[end] < input_list[middle]:
        return find_pivot_point(middle, end, input_list)

    # Edge case: If none of the previous tests found the pivot location then 
    # this is a completely ordered array (not a rotated one)
    else:
        return start

    
def binary_search(start, end, input_list, number):
    """
    Binary search over an ordered array (ascending).
    Args:
        start(int), end(int): indexes for a search interval
        input_list(array): Input array to search
        number(int): target number
    Returns:
        int: Number index or -1
    """

    # Stop condition: Unordered vector part of size 2 means the 
    # last element is the minimum one
    if (end - start) <= 1:
        if number == input_list[start]:
            return start
        elif number == input_list[end]:
            return end
        else:
            return -1

    # The segment (start through end) is divided in two parts by a middle index
    middle_index = (end - start) // 2 + start
    middle_value = input_list[middle_index]

    # If the number is in the first half, look there and discard the second half
    if number < middle_value:
        return binary_search(start, middle_index-1, input_list, number)
    # Otherwise look at the second half
    else:
        return binary_search(middle_index, end, input_list, number)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    size = len(input_list) 

    # Edge cases treatment
    if size == 0 or type(number) != int:
        return -1

    # Finds the pivot point location (index to the lowest value in the array)
    pivot = find_pivot_point(0, size-1, input_list)

    # Divides the search into two parts. At first, try to find the number 
    # among the lowerest values from the pivot point until the end of the array
    index = binary_search(pivot, size-1, input_list, number)
    if index != -1:
        return index
    else:
        # If not found, try to find it among the greatest values, from the 
        # begining of the array until the pivot point
        return binary_search(0, pivot-1, input_list, number)



# Test cases


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")



print('\n# Test case 1: Examples from the problem statement')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# It is expected to pass all tests



print('\n# Test case 2: An arbitrary array')
some_array = []
pivot = random.randint(0, 1000)
for n in range(pivot, 1000, 5):
    some_array.append(random.randint(n, n+4))
for n in range(0, pivot, 5):
    some_array.append(random.randint(n, n+4))
a_number = random.randint(0, 1000)
index = rotated_array_search(some_array, a_number)

print("Number: {}\n{}\nIndex: {}".format(a_number, some_array, index))
test_function([some_array, a_number])
# It is expected to pass test and also show the array, number and search result



print('\n# Test case 3: An ordered array. No rotation')
print('# A search for a number in every array position')
an_array = list(range(7))
for n in range(7):
    test_function([an_array, n])
# It is expected to pass all tests



print('\n# Test case 4: Edge case. One empty array')
print(rotated_array_search([], 6))
test_function([[], 6])
# It is expected to pass the test and return -1



print('\n# Test case 5: Edge case. Search for a non integer value')
print(rotated_array_search([1, 2, 3, 4, 5, 6], '6'))
test_function([[1, 2, 3, 4, 5, 6], '6'])
# It is expected to pass the test and return -1
