'''
Welcome to the queue tutorial!
'''
import random

class Queue:

    def __init__(self):
        # Initialize the queue as an empty array.
        self.queue = []

    def __str__(self):
        # return the queue as a string representation.
        return str(self.queue)
    
    # Remember when we enqueue we append to the back of an array. 
    def enqueue(self, value):
        self.queue.append(value)
        
        
    # Remember when we dequeue we remove from the front of an array.
    def dequeue(self):
        # If there is nothing in the queue print a message.
        if len(self.queue) <= 0:
            print('There is nothing in the queue.')

        value = self.queue[0]
        del self.queue[0]
        return value

    def dequeue_to_one_value(self):
        print(f'Completed array: {queue}')
        while len(self.queue) > 1:
            self.dequeue()
            print(f'dequeue: {queue} ')

    def enqueue_to_amount(self, amount, start, end):
        print(f'Empty array: {queue}')
        for _ in range(amount):
            self.enqueue(random.randint(start, end))
            print(f'enqueue a random number: {queue}')
        


queue = Queue()

# enqueue to the back. Ten numbers from values ranging from 1 to 10.
queue.enqueue_to_amount(amount=10, start=1, end=10)

print('\n---------------------------------------------------------\n')

# dequeue from the front.
queue.dequeue_to_one_value()






    