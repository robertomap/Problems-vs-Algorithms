# Udacity Data Structures and Algorithms
# Project 3 - Problem #4 - Dutch National Flag Problem

def sort_012(list012):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if type(list012) != list:
        return []

    # This indexes aim to point to the first and last position with number '1', if so.
    place_for_a_zero = 0
    place_for_a_two = len(list012) - 1

    # Index used to traverse the list
    i = 0

    while i <= place_for_a_two:
        if list012[i] == 0:
            list012[i], list012[place_for_a_zero] = list012[place_for_a_zero], list012[i]
            # Pushes foreward the index for possible first '1' position
            place_for_a_zero += 1
            # Advance to the next index to be evaluated
            i += 1
        elif list012[i] == 2:
            list012[i], list012[place_for_a_two] = list012[place_for_a_two], list012[i]
            # Pushes backward the index for possible last '1' position
            place_for_a_two -= 1
        else:
            # Advance to the next index to be evaluated
            i += 1
    
    return list012



# Test cases


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print('\n# Test case 1: Example from the problem statement')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# It is expected to pass all tests



print('\n# Test case 2: Lists with the same value for all items')
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
# It is expected to pass all tests



print('\n# Test case 3: Lists with only one item')
test_function([0])
test_function([1])
test_function([2])
# It is expected to pass all tests



print('\n# Test case 4: Edge Case: Empty list')
test_function([])
# It is expected to pass the test



print('\n# Test case 5: Edge Case: Not a list')
print(sort_012(2001022100))
# It is expected to return and print '[]'

