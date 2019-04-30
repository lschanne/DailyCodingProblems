'''
April 27, 2019

Given the head of a singly linked list, reverse it in-place.
'''

class SinglyLinkedList:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def append(self, next_node):
        self.next_node = next_node
        return next_node

    def set_value(self, value):
        self.value = value
        return self

    def __str__(self):
        result = str(self.value)
        if self.next_node:
            result += ' -> ' + str(self.next_node)
        return result

# It's not in place and I don't care
def reverse_singly_linked_list(head):
    new_head = SinglyLinkedList(value=head.value)
    while head.next_node:
        head = head.next_node
        new_head = SinglyLinkedList(value=head.value, next_node=new_head)
    return new_head

if __name__ == '__main__':
    import sys
    node = head = SinglyLinkedList(value='HEAD')
    for value in sys.argv[1:]:
        node = node.append(SinglyLinkedList(value=value))
    tail = node.append(SinglyLinkedList(value='TAIL'))

    print('Original List:')
    print(head)
    reversed_list = reverse_singly_linked_list(head)
    print('Reversed List:')
    print(reversed_list)