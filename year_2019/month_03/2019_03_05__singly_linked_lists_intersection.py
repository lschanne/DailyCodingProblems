'''
March 5, 2019

Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.
'''

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ' -> '
            string += str(self.next)
        return string

def get_length(X):
    x = X
    length = 1
    while x.next:
        x = x.next
        length += 1
    return length

# O(2 * M + 2 * N) == O(M + N), so I win :)
def get_intersection(A, B):
    len_a = get_length(A)
    len_b = get_length(B)

    a, b = A, B
    while len_a > len_b:
        a = a.next
        len_a -= 1
    while len_b > len_a:
        b = b.next

    # So this only works because A and B are the same length, but if they
    # weren't, it wouldn't
    while a.next:
        if a.value == b.value:
            return a.value

        a = a.next
        b = b.next

if __name__ == '__main__':
    intersect = Node(8, Node(10))
    A = Node(5, Node(3, Node(7, intersect)))
    B = Node(99, Node(1, intersect))
    print('A: {}'.format(A))
    print('B: {}'.format(B))
    print('intersection: {}'.format(get_intersection(A, B)))
