# Problem 7: Request Routing in a Web Server with a Trie

The algorithm input _**n**_ corresponds to the router trie size, being the number of nodes stored in it. Each node will represent a part of an URL string. The parameter _**s**_ corresponds to path string size in term of its parts.

The solution to this problem starts from a trie implementation similar to the one seen in Problem #5. Therefore, the analysis made for this Problem #7 will resemble to the previous one.

The algorithm considers a class _**Router**_, which will implement the main exterior interfaces: the _.add_handler()_ and _.lookup()_ methods. Aside from the computation for creating a list of parts by a helper _.split_path()_ method, which simply iterates over the input string, these two methods add no significant cost to the entire algorithm. Thus, the analysis will be carried out focusing on the trie structure used.

The _**RouteTrie**_ class implements a _.insert()_ method for adding a route path and its respective handler to the trie. The classe also implements a _.find()_ method that returns the handler corresponding to a giving path, or a 404 handler if not found.

Both _.insert()_ and _.find()_ methods perform a walk through the trie, and each step will correspond to actions of visiting or creating a new node. Both actions carry only _**O(1)**_ operations, so finding and inserting new path/handlers into the trie have an _**O(s)**_ time complexity. To performe the trie walk, these two methods firstly count on the _.split_path()_ helper method to create a list of parts, which is made by traversing the input URL string. This process also behaves as _**O(s)**_ and does not contribute to increase the time complexity.

The overall process of creating the entire trie data strucuture will perform as _**O(s*n)**_ time complexity. Regardless of the fact that the structure itself will have _**n**_ nodes, at each path/handler insertion process, a fraction of the nodes will have already been created and a visit action will be required anyway.

It would be reasonable to set a maximum path length to be stored in the trie structure as a constant value _**k**_, since it would have no point to manage an arbitrarely large path lenght, considering any typical Web Server application. However, this has not been implemented in this exercise. In this sense, this _.insert()_ and _.find()_ operations would have a maximum constant execution time.

Regarding to space, both _.insert()_ and _.find()_ methods use the auxiliary list of parts created by the _.split_path()_ helper method, which behaves as _**O(s)**_ space complexity. The _.insert()_ and _.find()_ methods themselves simply iterate over the list and make use of a few auxiliary variables, which represent _**O(1)**_ space complexity. The overall process will result in _**O(s)**_ space complexity.
The cost for storing the entire trie data structure itself will be _**O(n)**_, since it will have _**n**_ nodes.
