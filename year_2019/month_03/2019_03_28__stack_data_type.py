'''
March 28, 2019

Implement a stack that has the following methods:
- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack. If there
  are no elements in the stack, then it should throw an error or return null.
- max(), which returns the maximum value in the stack currently. If there are
  no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if self._stack:
            return self._stack.pop()

    def max(self):
        if self._stack:
            return max(self._stack)

# I did more of a dynamic testing for this one by importing it via iPython
