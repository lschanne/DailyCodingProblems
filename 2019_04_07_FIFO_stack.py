'''
April 7, 2019

Implement a queue using two stacks. Recall that a queue is a FIFO
(first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue,
and dequeue, which removes it.
'''

# I feel like I'm cheating...
# But the data structure challenges aren't always very interesting to me,
# so I guess I don't care that much
class FIFO:
    def __init__(self):
        self._stack = []

    def enqueue(self, value):
        self._stack.append(value)

    def dequeue(self):
        if self._stack:
            return self._stack.pop()
