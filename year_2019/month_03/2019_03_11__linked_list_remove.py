'''
March 11, 2019

Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

class SinglyLinkedList:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.length = 1
        if self.next_node:
            self.length += self.next_node.length

    def __str__(self):
        string = str(self.value)
        if self.next_node:
            string += ' -> ' + str(self.next_node)
        return string

    # This method is the actually problem
    def remove_recurse(self, k, idx=0):
        if self.next_node:
            if k - idx <= 1:
                if k - idx <= 1:
                    self.value = self.next_node.value
                if not self.next_node.next_node:
                    self.next_node = None
            self.next_node.remove_recurse(k, idx + 1)
        else:
            raise IndexError(
                "k = {} is out of range.".format(k)
            )

    # Well I don't know if this is totally optimal, because we have to iterate
    # over the entire list each time, but at least it's better than recursion
    def remove(self, k):
        if not 0 <= k < self.length:
            msg = "k={} is out of range.".format(k)
            raise IndexError(msg)

        current = self
        next_node = self.next_node
        idx = 0
        while next_node and next_node.next_node:
            current.length -= 1
            idx += 1
            if idx >= k:
                current.value = current.next_node.value
            current = next_node
            next_node = current.next_node

        # if/else here should only be for the case of length==1
        current.value = next_node.value if next_node else None
        current.next_node = None

if __name__ == '__main__':
    import sys
    k = int(sys.argv[1])
    my_list = None
    for val in reversed(sys.argv[2:]):
        my_list = SinglyLinkedList(val, my_list)

    print('k: {}'.format(k))
    print('my_list: {}'.format(my_list))
    if my_list:
        print('Removing the kth element...')
        my_list.remove(k)

    print('my_list: {}'.format(my_list))