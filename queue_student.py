'''
Welcome to the Student problem. You are working for Visa at a call center.
You are assigned to a desk and aked to take clients calls all day long. 
When a call is completed it should be removed from the queue and you are
asked to take the next phone call. You can go home when all the calls are 
completed and the queue is empty. 

Complete the remaining methods in the Queue class. 
What you need to code will be layed out with #Student code goes here. The
instruction are commented out.

Have Fun! If you spend more than two hours looking at this and cannot
figure it out go ahead and look at the solution for help. When done make sure
to compare solutions. If you come up with a better one I would love to know. 
My contact information is on the home page.
'''

import random

class Queue:
    def __init__(self):
        # Initialize the queue as an empty array.
        self.queue = []


    def __str__(self):
        # return the queue as a string representation.
        return str(self.queue)

    def enqueue_phone_number(self):
    # Create a method that enqueues phone calls.
    # Step 1: Prompt the user for a number of phone calls to generate.
    # Step 2: call the random_phone_num_generator and append the calls to the
    # queue.
    # Step 3: print the queue.
    
    # STUDENT CODE GOES HERE!
        pass

    def dequeue_call(self):  
    # Create a method that dequeues calls.
    # Hint: Remember that dequeue is removing from the front of a list!
    # STUDENT CODE GOES HERE!
        pass
        

    def complete_call(self):
    # Create a while loop that asks the employee if the call is complete. 
    # If the worker types "y" the call should be dequeued and the queue 
    # should be updated and printed. 
    # If the worker types "n" a message should print "Get back to work!"
    # If there are no more calls in the queue the work is finished and a 
    # message should display "Time to go home!"

    #STUDENT CODE GOES HERE!
        pass

    
    def random_phone_num_generator(self):
        # This method generates a random phone number to simulate incoming calls. 
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = str(random.randint(1, 9998)).zfill(4)
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))
        return '{}-{}-{}'.format(first, second, last)
    



queue = Queue()

# call the enqueue call method
queue.enqueue_phone_number()

# Call the complete call method
queue.complete_call()
