'''
This program gives the starter code for a binary search tree.
The student needs to finish the functions that will return the 
smallest and largest values in the tree. 
'''

import random

class BST():


    class Node():
        '''
        Remember with a binary search tree each node links to either a left
        or right sub tree.
        '''

        def __init__(self,data):
            '''
            Initialize pointers for each node. There is nothing in the tree 
            at first so set variables to none.
            '''
            self.data = data
            self.left = None
            self.right = None
        
    
    def __init__(self):
        '''
        Create an empty BST.
        '''
        self.root = None

    
    def insert(self,data):
        '''
        Put the data into the BST
        '''
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    
    def _insert(self,data,node):
        '''
        This function will find the correct place to insert the data into the BST.
        remember that smaller values go to the left and larger values go to the right.
        '''
        if data < node.data and data != node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data and data != node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)


    def __contains__(self, data):
        """ 
        return the node being searched for if it exists in the tree.
        """
        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):
        """
        Search for the node.
        """
        # Base Cases.
        if node is None:
            return False
        
        if data == node.data:
            # print('true')
            return True

        # Recursion.
        elif data < node.data:
            return self._contains(data, node.left)
 
        elif data > node.data:
            return self._contains(data, node.right) 


    def smallest_node(self):
        '''
        The student must write a funtion that recursivley calls to find the
        smallest node in the tree.
        '''

        return self._smallest_node(self.root)


    def _smallest_node(self,node):
        '''
        The student must write a funtion that recursivley calls to find the 
        largest node in the tree.
        '''

        # Base Case:
        if node.left == None:
            return node.data

        # Recursion:
        return self._smallest_node(node.left)


    def largest_node(self):
        '''
        The student must write a funtion that recursivley calls to find the 
        largest node in the tree.
        '''

        return self._largest_node(self.root)

 
    def _largest_node(self,node):
        '''
        This function will recrusivley work its way through the right side
        of the tree to find the largest.
        '''
        
        # Base Case.
        if node.right == None:
            return node.data
        
        # Recursion.
        return self._largest_node(node.right)


    def __iter__(self):
        '''
        Allow us to traverse through the tree starting at the root.
        '''
        yield from self._traverse_forward(self.root)  # Start at the root


    def _traverse_forward(self, node):
        """
        Yield allows us to loop through the tree and get all the values.
        Start on the left and get all the smaller numbers then work on
        the right side of the tree and get all the larger numbers
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


# Create a BST object.
tree = BST()


# Ask for user input to create and search the tree.
insert_tree = int(input('Enter an integer to create a tree. '))


# Insert into the tree the specified amount of times.
try:
    for _ in range(insert_tree):
        tree.insert(random.randint(1,100))
except:
    print('Try again and enter a valid integer.')


# Print all the nodes in the tree.
print('The nodes in the tree are.')
for x in tree:
    print(x)


# Print the largest and smallest nodes in the tree.
print(f'The smallest node in the tree is: {tree.smallest_node()}')

print(f'The largest node in the tree is: {tree.largest_node()}')