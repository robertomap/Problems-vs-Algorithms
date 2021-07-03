# Udacity Data Structures and Algorithms
# Project 3 - Problem #5 - Autocomplete with Tries
 
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        # Stop condition for recursion        
        if self.children is None:
            return []

        # It recursively builds up a suffix list based on a giving prefix
        suffix_list = []

        # It implements a DFS starting from the prefix location
        for char in self.children:

            # Every time it findig a match as a word the list get appended
            if self.children[char].is_word == True:
                suffix_list.append(suffix + char)

            # It goes deeper into the tree and concatenates the new results
            # with the ones already obtained. 
            suffix_list += self.children[char].suffixes(suffix + char)

        return suffix_list


## The Trie itself containing the root node and insert/find functions
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix

        # Edge case: Treating not valid prefixes
        if type(prefix) != str or prefix == '':
            return TrieNode()

        # Walks through the trie and returns the location (node reference)
        # corresponding to the giving prefix. It returns an empty node if 
        # the prefix is not found.
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return TrieNode()
        return node        



# Test Cases



MyTrie = Trie()
wordList = [
    "an", "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "fact", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



print("\nTest Case 1: Testing it all out - Interactive")
# Run the following code to add some words to your trie 
# and then use the interactive search box to see what your code returns.
# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');
print("It is expected to return the correct suffixes in the ")
print("Jupyter Notebook interactive window.")



print("\nTest Case 2: Some examples")
prefix = 'a'
prefixNode = MyTrie.find(prefix)
print("Prefix: '{}'".format(prefix))
print(prefixNode.suffixes())

prefix = 'ant'
prefixNode = MyTrie.find(prefix)
print("Prefix: '{}'".format(prefix))
print(prefixNode.suffixes())

# It is expected to return the corresponding suffixes.



print("\nTest Case 3: Edge Case - Empty prefix")
prefix = ''
prefixNode = MyTrie.find(prefix)
print(prefixNode.suffixes())
# It was implemented so it do not returns any suffixes. 
# So it is expected to return an empty list.



print("\nTest Case 4: Edge Case - Invalid numeric prefix")
prefix = ''
prefixNode = MyTrie.find(prefix)
print(prefixNode.suffixes())
# It was implemented so it do not returns any suffix and avoid 
# runtime errors. So it is expected to return an empty list.
