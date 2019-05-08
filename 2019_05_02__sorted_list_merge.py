'''
May 2, 2019

Given k sorted singly linked lists, write a function to merge all the lists
into one sorted singly linked list.
'''

class SinglyLinkedList:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        string = str(self.value)
        if self.next_node:
            string += ' -> {}'.format(self.next_node)
        return string

    def __eq__(self, other_list):
        return (
            isinstance(other_list, SinglyLinkedList) and
            self.value == other_list.value and
            self.next_node == other_list.next_node
        )

def generate_list(*values):
    head = None
    for x in values:
        if head is None:
            head = tail = SinglyLinkedList(x)
        else:
            tail.next_node = SinglyLinkedList(x)
            tail = tail.next_node
    return head

def sorted_list_merge(*input_lists):
    head = None
    input_lists = [x for x in input_lists if x is not None]
    finished = 0
    while finished < len(input_lists):
        min_value = float('inf')
        for idx, node in enumerate(input_lists):
            if node is None:
                continue
            if node.value < min_value:
                min_value = node.value
                min_idx = idx
        if head is None:
            head = tail = SinglyLinkedList(min_value)
        else:
            tail.next_node = SinglyLinkedList(min_value)
            tail = tail.next_node
        input_lists[min_idx] = input_lists[min_idx].next_node
        if input_lists[min_idx] is None:
            finished += 1
    return head

if __name__ == '__main__':
    for input_lists, expected_result in (
        (
            [
                generate_list(1, 2, 3),
                generate_list(4, 5, 6),
                generate_list(7, 8, 9),
            ],
            generate_list(1, 2, 3, 4, 5, 6, 7, 8, 9)
        ),
        (
            [
                generate_list(3, 3, 3),
                generate_list(1, 1, 2, 2),
                generate_list(5),
            ],
            generate_list(1, 1, 2, 2, 3, 3, 3, 5)
        ),
        (
            [
                generate_list(1, 1, 2, 2, 3, 3, 4, 4),
                generate_list(1, 2, 3, 4),
            ],
            generate_list(1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4)
        ),
    ):
        print('input lists:')
        for x in input_lists:
            print('    {}'.format(x))
        print('expected output: {}'.format(expected_result))
        result = sorted_list_merge(*input_lists)
        print('actual   output: {}'.format(result))
        print('test passed: {}'.format(result == expected_result))
