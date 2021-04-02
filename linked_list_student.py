'''
Congratulations! You made it to module two. As mentioned in module one there
is a better way to impliment the queue. We will use a linked list to impliment
the same call center scenario. We will enqueue a certain number of calls for the
days work. Once a call is completed it should be dequeued from the linked list.

The performance of dequeueing or removing from the front with an array is O(n) 
because every element in the array has to shift over one index. 

The performance of dequeueing or removing from the front with a linked list is
O(1) because each node has pointers in computer memory that reveal the location
of the next node. All we have to do is remove the pointers and set the correct 
node to the head. This can be done in O(1) time.
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
        This function should insert a new node at the tail or end of the linked
        list.

        The student must:
        complete the enqueue_linked_list function.
        '''

        pass
        # Hint: remember the important note that if there is nothing in the queue we need
        # to set the new node to the head and tail.
        
        # Hint: "If" there is nothing in the linked list we should handle that case. "Else" we
        # should enqueue from the back. 
    
    def dequeue_linked_list(self):
        '''
        This function should remove the node at the beginning of the linked list
        which is the "head"
        
        Remember the important note if there is only one item in the list the head
        and the tail will need to be set to None. This essentialy creates an empyt
        list.

        The student must:
        complete the dequeue_linked_list function.
        '''
        pass
        # Hint: This is the same as removing from the head.


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

# Call the complete call function. This function will dequeue calls from 
# the linked list. 
ll.complete_call()
