'''
February 19, 2019

An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is
an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index)
which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
'''

class Element:
    def __init__(self, value, ptr):
        self.value = value
        self.both = ptr

    def next(self, ptr):
        self.both ^= ptr

class XORLinkedList:
    def __init__(self):
        # just pretending that python uses pointers
        self.cursor = self.ptr = 0
        self.head = None
        self.pointers = {}

    def add(self, value):
        prev = self.cursor
        self.cursor += 1
        self.pointers[self.cursor] = Element(value, prev)
        if self.head:
            self.pointers[prev].next(self.cursor)
        else:
            self.head = self.cursor

    def get(self, index):
        prev = self.ptr
        ptr = self.head
        while index:
            index -= 1
            prev, ptr = ptr, prev ^ self.pointers[ptr].both
        return self.pointers[ptr].value

if __name__ == '__main__':
    l = XORLinkedList()
    for v in range(5):
        l.add(v)

    for idx in range(5):
        print(l.get(idx))