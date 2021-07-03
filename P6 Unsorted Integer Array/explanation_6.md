# Problem 6: Unsorted Integer Array

The algorithm input ***n*** corresponds to the unsorted integer array size.

To solve this problem the `get_min_max()` function simply traverses the list and compares each element with `max` and `min` auxiliar variables, which are both initialized with the first item in the array. Higher and lower values found along the array traversal are stored in these variables, which guarantees that they get the highest and lowest possible values at the end of the traversal.

No special data strucuture was needed in this solution, since it is only necessary to store two integer values that represent the lowest and the highest numerical values along the iteractive traversal.

The algorithm performs a couple of numeric comparisons for each element in the list, so the time complexity 
results in ***O(n)***.

Since the algorithm uses only a couple of auxiliaries, the space complexity results in ***O(1)***.
