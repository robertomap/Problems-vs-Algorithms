# Udacity Data Structures and Algorithms
# Project 3 - Problem #7 - Request Routing in a Web Server with a Trie

# A RouteTrie that stores routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, not_found_handler):
        # Initializes the trie with an root node and a handler.
        # This is the root path or home page node.
        self.root = RouteTrieNode()
        self.root.handler = handler
        self.not_found_handler = not_found_handler


    def insert(self, path_list, handler):
        """
        Add `route` with its respective handler to the Trie
        If successful, returns 'True' if not 'False'.
        """

        # Edge case: Not a valid path string
        if path_list == []:
            return False

        current_node = self.root

        # Walks through the trie and insert only new parts
        for part in path_list:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]

        # Applies the handler to the last part node
        current_node.handler = handler

        return True


    def find(self, path_list):
        """
        Look for a match for a giving path.
        Returns the ´handler´ for a match, a ´not found handler´ for no match, 
        or None for an empty path.
        """

        # Returns home handler
        if path_list == ['/']:
            return self.root.handler

        # Edge case: Empty path treatment
        if path_list == []:
            return None

        node = self.root

        # Checks if the path is found
        for part in path_list:
            if part in node.children:
                node = node.children[part]
            else:
                return self.not_found_handler
        
        # Checks if the path has a hadler
        if node.handler:
            return node.handler
        else:
            return self.not_found_handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initializes the node with children as before, plus a handler
        self.handler = None
        self.children = {}


    def insert(self, part):
        """
        Helper method to insert a node.
        """
        # Inserts the node as before
        self.children[part] = RouteTrieNode()




# The Router class that wraps the Trie and handles 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Creates a new RouteTrie for holding the routes
        self.trie = RouteTrie(root_handler, not_found_handler)


    def add_handler(self, path, handler):
        """
        Add a handler for a path.
        If successful, returns 'True' if not 'False'.
        """

        # split a string into parts getting rid of '/'
        path_list = self.split_path(path)

        # Inserts the path and handler into the trie
        return self.trie.insert(path_list, handler)


    def lookup(self, path):
        """
        Lookup path (by parts) and return the associated handler
        It returns the "not found" handler if the path is not found
        """

        # split a string into parts getting rid of '/'
        path_list = self.split_path(path)

        # returns the correspondent handler
        return self.trie.find(path_list)



    def split_path(self, path):
        """
        Split the path into parts.
        It returns a list of parties
        """
        
        # Returns an empty list for an empty path
        if path == "":
            return []

        # Returns a "/" to indicate root path
        if path == "/":
            return ["/"]

        return path.strip('/').split('/')




# Test Cases

# Creates the router with root and 404 handlers
router = Router("root handler", "not found handler")


print('\n# Test Case 1: Adds somes routes and handlers')
print(router.add_handler("/home/about", "about handler")) 
print(router.add_handler("/home/contact", "contact handler"))
# Add a route and return ´True´ as a confirmation for both

print('\n# Test Case 2: Add a path that consists of part of an existing one.')
print(router.add_handler("/home", "home handler"))
# Add a route and return ´True´ as a confirmation 

print('\n# Test Case 3: Edge case: Empty path string')
print(router.add_handler("", "not valid handler"))  
# Expected nothing to be added and return ´False´ as confirmation


# Some lookups with the expected outputs

print('\n# Test Case 4: Look for the root handler')
print(router.lookup("/")) 
# should print 'root handler'


print('\n# Test Case 5: Look for some handlers')
print(router.lookup("/home")) # should print 'home handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/contact")) # should print 'contact handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'


print('\n# Test Case 6: Edge case: Look for some path with a typo')
print(router.lookup("/home//about/")) 
# should print 'not found handler'


print('\n# Test Case 7: Edge case: Look for and empty path string')
print(router.lookup("")) 
# should print 'None'
