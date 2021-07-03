# Udacity Data Structures and Algorithms
# Project 3 - Problem #3 - Rearrange Array Elements

  
def mergesort(items):
    """
    Merge sort algoithm.

    Args:
       items(list): Input array to be sorted
    Returns:
       list: sorted array
    """

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge_reversed(left, right)


def merge_reversed(left, right):
    """
    Merge helper function which merges two lists in a descending order

    Args:
       left(list), right(list): Arrays to be merged
    Returns:
       list: merged array 
    """
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List of integers [0, 9]
    Returns:
       (int), (int): Two maximum sums
    """

    # Edge cases treatment: Input array of size 0
    if len(input_list) == 0:
        return 0, 0

    # Edge cases treatment: Invalid array element
    for n in input_list:
        if type(n) != int or n < 0 or n > 9:
            return 0, 0

    # Input array ordered (descending) 
    ordered_list = mergesort(input_list)

    # Then it equally distributes the array number elements into the two 
    # reaulting numbers. The higher the number in the array the more significant
    # digit it will represent in the final result.
    num1 = 0
    for i in range(0, len(ordered_list), 2):
        num1 = num1*10 + ordered_list[i]

    num2 = 0
    for i in range(1, len(ordered_list), 2):
        num2 = num2*10 + ordered_list[i]
    
    return num1, num2



# Test cases


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print('\n# Test case 1: Example from the problem statement')
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# It is expected to pass the test


print('\n# Test case 2: Two arrays with even and odd sizes')
test_function([[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7], [7654321, 7654321]])
test_function([[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7], [7654321, 654321]])
# It is expected to pass all tests


print('\n# Test case 3: Array that is already ordered (descending)')
test_function([[9, 8, 7, 6, 5, 4, 3, 2, 1], [97531, 8642]])
# It is expected to pass the test


print('\n# Test case 4: Input array of size 1')
print(rearrange_digits([1]))
test_function([[1], [1, 0]])
# It is expected to pass the test by producing a (1, 0) result


print('\n# Test case 5: Edge case: Input array of size 0')
print(rearrange_digits([]))
test_function([[], [0, 0]])
# It is expected to pass the test by producing a (0, 0) result


print('\n# Test case 6: Edge case: Invalid array elements')
test_function([[1, 2, '3', 4, 5], [0, 0]])
test_function([[1, 2, -3, 4, 5], [0, 0]])
# It is expected to pass the tests by producing (0, 0) as result
