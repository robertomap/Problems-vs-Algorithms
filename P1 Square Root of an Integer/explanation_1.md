# Problem 1: Square Root

The algorithm input ***n*** will correspond to the size of the number for which the floor square root is expected.

This problem could be solved by simply testing all the possibilities, guessing one by one, from zero to the one that solves for the given number.  Instead, the algorithm uses some kind of _educated guess_ in order to faster approximate the solution. For this, the function `mysqrt()` implementation resembles a binary search, in which half of the possible solutions are eliminated in each iteration of the `while` loop, simply by pointing to the middle of the numerical range being analyzed. Once the exact square is found or the numerical range narrows to the size of only one integer, which indicates a floored solution, the algorithm skips the loop. No special data strucuture was needed in this solution, since it is only necessary to store the integer values that represent the first and the last value of the numerical range being analyzed.

The simple one-by-one guess approach would result in a ***O(n)*** behaviour. On the other hand, the binary search implementation used here is performed logarithmically. Since each iteration uses only ***O(1)*** operations, this approach lead to a ***O(log n)*** time complexity.

Regarding to space, the algorithm uses only a couple of integer auxiliaries. Since they do not depend on the giving number, it will result in an ***O(1)*** space complexity.

