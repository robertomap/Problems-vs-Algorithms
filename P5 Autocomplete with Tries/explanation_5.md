# Problem 5: Autocomplete with Tries

The algorithm input _**n**_ corresponds to the trie size, being the number of nodes stored in it. And the parameter _**s**_ corresponds to size of the giving prefix.

Since the focus of this exercise is on autocomplete operation, this analysis leaves out the complexity of creating and storing a trie structure. 

The solution for this problem starts from a trie implementation just like the one seen in the Basic Algorithm Lesson. The additional _.find()_ method implemented here returns the location in the trie (node reference) corresponding to a giving prefix. The _.suffixes()_ method implements a recursive DFS in the sub-tree starting from the prefix node and returns a list of correspondent suffixes. 

The _.find()_ method iterates over the prefix of size s and will behave as _**O(s)**_ since the nested dictionary (hash map structure) allows _**O(1)**_ operations at each trie level. It would be reasonable to set a maximum size of a word stored in the structure as a constant value k, since this structure is intended for word completion, although this has not been implemented in this exercise. In this sense, this _.find()_ operation would have maximum constant time.

The _.suffixes()_ method will walk through the strcucture from the prefix node given and reach the end of all possible branches. This algorithm considers a prefix of at least one character. So in this worst case, the algorithm needs to walk through a considerable fraction of the entire input n. For the sake of simplicity, we can think that this “fraction” may grow linearly in relation to the growth of the input. In this sense the suffix seach would behave as _**O(n)**_ time complexity. 

Based on the above considerations, the general operation of finding a prefix node and returning the list of suffixes results in O(n) time complexity.

Regarding to space, the _.find()_ method utilizes only a few auxiliaries and a loop operation based on a Python iterator, which results in _**O(1)**_ space complexity. On the other hand, the _.suffixes()_ method is based on a recursive approach and needs to stack up a function call for each node along all possible branches, starting from the prefix given node. Taking into account the same considerations made above for time complexity, it would result in a _**O(n)**_ space complexity. 
