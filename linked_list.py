'''
This is an example of how to impliment a linked list. 
'''

class Linked_list:


    class Node:

        def __init__(self,data):
            '''
            Create a constructor that keeps track of datas value, the next
            and previous nodes.
            '''
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        '''
        Create a constructor that initializes an empty list
        '''
        self.head = None
        self.tail = None

    # Now we have our linked list created and the pointers needed to identify
    # each Node. We will now need to add functions that can
    # 1. Insert from the head.
    # 2. Insert from the tail.
    # 3. Insert in the middle.
    # 4. Remove from the head.
    # 5. Remove from the tail. 
    # 6. Remove from the middle. 


    # 1. Insert from the head.
    def insert_at_head(self, value):
        '''
        This function will insert a new node at the head or the beginning
        of a linked list. 
        '''
        # Create a new_node step #1
        new_node = Linked_list.Node(value)

        # Remember the important note that said if the list is empty to set 
        # the head and tail to the new node. 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            # Set the pointer of the new node to the original head. Step #2
            new_node.next = self.head

            # Set the previous pointer of the original head to the new node.
            # Step #3
            self.head.prev = new_node

            # Set the head equal to the new node. Step #4
            self.head = new_node


    # 2. Insert from the tail.
    def insert_at_tail(self,value):
        '''
        This function will insert a new node at the tail or end of the linked
        list.
        '''

        # Create a new node called new_node. Step #1
        new_node = Linked_list.Node(value)

        # Set the previous pointer of the new node to be the tail. Step #2
        new_node.prev = self.tail

        # Set the next pointer of the original tail to the new node. Step #3
        self.tail.next = new_node

        # Set the tail equal to the new node. Step #4
        self.tail = new_node


    # 3. Insert in the middle.
    def insert_at_middle(self, value, new_value):
        '''
        This function will insert a new node in the middle of a linked list.
        Remember this can be tricky. Make sure to follow the steps in the correct
        order.
        '''
        # Remember we cannot look up by index with a linked list. We need to search
        # for the node that we want to insert after. To do this we can start at the 
        # head.
        current = self.head
        
        # Make sure there is a head to start with.
        while current is not None:
            if current.data == value:
            # If we are at the end of the list we can just call insert_at_tail.
                if current == self.tail:
                    self.insert_at_tail(new_value)
                
                else:
                    # Create a new node called new node. Step #1
                    new_node= Linked_list.Node(new_value)

                    # Set the previous pointer of the new node to current.node Step #2
                    new_node.prev = current

                    # Set next pointer of the new node to the next node after current.
                    # Step #3
                    new_node.next = current.next

                    # Set previous pointer of the node after current to the new node.
                    # Step #4
                    current.next.prev = new_node

                    # Set the next pointer of the current node to the new node. Step #5
                    current.next = new_node

                # Exit the function
                return 
            # Go to the next node and search for the value.
            current = current.next


    # 4. Remove from the head.
    def remove_head(self):
        '''
        This function will remove the node at the beginning of the linked list
        which is the "head"
        
        Remember the important note if there is only one item in the list the head
        and the tail will need to be set to none. This essentialy creates an empyt
        list.
        '''
        if self.head == self.tail:
            self.head == None
            self.tail == None

        elif self.head is not None:
            # Set previous pointer of the second node to node. Step #1
            self.head.next.prev = None

            # Set the head to be the second node.
            self.head = self.head.next
    

    # 5. Remove from the tail. 
    def remove_tail(self):
        '''
        This function will remove a node from the linked list at the "tail" which 
        is the end of the list.
        '''

        # Set next pointer of second to last node to none. Step #1
        self.tail.prev.next = None

        #Set the tail to be teh second to last node. Step #2
        self.tail = self.tail.prev
    

    # 6. Remove from the middle.
    def remove_middle(self, value):
        # Remember we cannot look up by index with a linked list. We need to search
        # for the node that we want to insert after. To do this we can start at the 
        # head.
        current = self.head

        # Check if the value being removed is the head. If so just call the 
        # remove head function.
        if self.head.data == value:
            self.remove_head()
            return
        
        if self.tail.data == value:
            self.remove_tail()
            return
        
        # Loop through nodes until the correct one is found.
        while current is not None:

            if current.data == value:
                # If the correct node is found we need to remove it. Remember this
                # is a two step process. 

                # Set previous pointer of the node after current to the node before
                # current.
                current.next.prev = current.prev

                # Set the next pointer of the node before current to the node after
                # current. Step #2
                current.prev.next = current.next
            current = current.next
    


    def __iter__(self):
        """
        Start at the beginning of the linked list and iterate through each node.
        """
        # Start at the beginning.
        curr = self.head 
        # Loop through each node until we are through the entire list.
        while curr is not None:
            yield curr.data 
            curr = curr.next 


    def __str__(self):
        """
        Gives us a string representation of what our linked list looks like.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

# Create linked list object.
ll = Linked_list()

# Insert at the head. Notice when we insert from the head each time I have
# to count backwards for the numbers to be in order.
ll.insert_at_head(5)
ll.insert_at_head(4)
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)
print(ll)
# Output: [1,2,3,4,5]

# Insert at the tail.
ll.insert_at_tail(9)
ll.insert_at_tail(10)
ll.insert_at_tail(11)
print(ll)
# Output: [1,2,3,4,5,9,10,11]

# Insert at the middle.
ll.insert_at_middle(5,6)
ll.insert_at_middle(6,7)
ll.insert_at_middle(7,8)
print(ll)
# Output: [1,2,3,4,5,6,7,8,9,10,11]

# Remove from the head.
ll.remove_head()
ll.remove_head()
ll.remove_head()
print(ll)
# Output: [4,5,6,7,8,9,10,11]

# Remove from the tail.
ll.remove_tail()
ll.remove_tail()
ll.remove_tail()
print(ll)
# Output: [4,5,6,7,8]

# Remove from the middle.
ll.remove_middle(6)
ll.remove_middle(7)
print(ll)
# Output: [4,5,8]

        

        






        

