'''
Here is my solution to implimenting a queue with an array.
Contact me if you have any questions or comments on how I can 
improve this tutorial.
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
        n = int(input("Enter a number to generate incomming calls: "))
        for _ in range(0, n):
            self.queue.append(self.random_phone_num_generator())
        print(self.queue)

    def dequeue_call(self):  
    # Create a method that dequeues calls.
    # Hint: Remember that dequeue is removing from the front of a list!
        del self.queue[0]
        

    def complete_call(self):
    # Create a while loop that asks the employee if the call is complete. 
    # If the worker types "y" the call should be dequeued and the queue 
    # should be updated and printed. 
    # If the worker types "n" a message should print "Get back to work!"
    # If there are no more calls in the queue the work is finished and a 
    # message should display "Time to go home!"
    
        call_complete = ''
        
        while len(self.queue) > 0:
            call_complete = input('Type y to complete the call. press n to quit. ')

            if call_complete == 'y':
                self.dequeue_call()
                print(self.queue)
            
            elif call_complete == 'n':
                print("Get back to work! ")
            
        print('There is nothing in the queue. Time to go home! ')

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