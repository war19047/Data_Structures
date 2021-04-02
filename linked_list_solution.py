'''
Here is my solution to implimenting a queue with a linked list.
Contact me if you have any questions or comments on how I can 
improve this tutorial.
'''

import random

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

    def random_phone_num_generator(self):
        # This function generates a random phone number to simulate incoming calls. 
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = str(random.randint(1, 9998)).zfill(4)
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))
        return '{}-{}-{}'.format(first, second, last)


    def enqueue_linked_list(self,value):
        '''
        This function will insert a new node at the tail or end of the linked
        list.
        '''

        # Create a new node called new_node.
        new_node = Linked_list.Node(value)

        # If the linked list starts out as empty. We need to insert a value. 
        # We cannot insert at the end or enqueue because there are no values 
        # in the linked list. We need to insert one time at the head if the
        # linked list is empty. Otherwise insert at the tail.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            # Set the previous pointer of the new node to be the tail. 
            new_node.prev = self.tail

            # Set the next pointer of the original tail to the new node. 
            self.tail.next = new_node

            # Set the tail equal to the new node.
            self.tail = new_node

    
    def dequeue_linked_list(self):
        '''
        This function will remove the node at the beginning of the linked list
        which is the "head"
        
        Remember the important note if there is only one item in the list the head
        and the tail will need to be set to none. This essentialy creates an empyt
        list.
        '''
        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head is not None:
            # Set previous pointer of the second node to none.
            self.head.next.prev = None

            # Set the head to be the second node.
            self.head = self.head.next

    def complete_call(self):
    # Create a while loop that asks the employee if the call is complete. 
    # If the worker types "y" the call should be dequeued and the queue 
    # should be updated and printed. 
    # If the worker types "n" a message should print "Get back to work!"
    # If there are no more calls in the queue the work is finished and a 
    # message should display "Time to go home!"
        
        while self.head is not None:
            call_complete = input('Type y to complete the call. press n to quit. ')

            if call_complete == 'y':
                self.dequeue_linked_list()
                print(self)
            
            elif call_complete == 'n':
                print("Get back to work! ")
            

        print('There is nothing in the queue. Time to go home! ')
    

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


ll = Linked_list()

# Ask the employee how many calls there are to take. 
enqueue = int(input("How many incomming calls are there? "))

# Start the work day with 15 phone calls. You can leave when they are 
# all completed.......
for _ in range(enqueue):
    ll.enqueue_linked_list(ll.random_phone_num_generator())
    print(ll)

print(ll)

# Call the complete call function. This function will dequeue calls from 
# the linked list. 
ll.complete_call()


