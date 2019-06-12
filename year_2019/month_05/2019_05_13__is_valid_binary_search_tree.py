'''
May 13, 2019

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies
the constraint that the key in the left child must be less than or equal to the
root and the key in the right child must be greater than or equal to the root.
'''

def is_valid_binary_search_tree(node):
    return (
        all(hasattr(node, attr) for attr in ('left', 'right', 'value')) and
        (
            node.left is None or
            (
                is_valid_binary_search_tree(node.left) and
                isinstance(node.left.value, int) and
                node.left.value <= node.value
            )
        ) and
        (
            node.right is None or
            (
                is_valid_binary_search_tree(node.right) and
                isinstance(node.right.value, int) and
                node.right.value >= node.value
            )
        )
    )

if __name__ == '__main__':
    class BinaryTree:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    test_objects = []

    ## Test 1 ##
    bst = BinaryTree(
        0,
        left=BinaryTree(
            -5,
            left=BinaryTree(-10),
            right=BinaryTree(-5),
        ),
        right=BinaryTree(5),
    )
    test_objects.append((bst, True))

    ## Test 2 ##
    just_a_tree = BinaryTree(
        0,
        left=BinaryTree(2),
        right=None,
    )
    test_objects.append((just_a_tree, False))

    ## Test 3 ##
    non_int_tree = BinaryTree(
        'a',
        left=BinaryTree('b'),
        right=BinaryTree('c'),
    )
    test_objects.append((non_int_tree, False))

    ## Test 4 ##
    not_even_a_tree = BinaryTree('wut', 'are', 'you?')
    test_objects.append((not_even_a_tree, False))

    ## Test 5 ##
    string = "I like to try to break tests"
    test_objects.append((string, False))

    all_passed = True
    for test_number, (test_input, expected_result) in enumerate(test_objects):
        test_number += 1
        try:
            result = is_valid_binary_search_tree(test_input)
        except Exception:
            print('test #{} threw an exception!'.format(test_number))
            all_passed = False
        else:
            if expected_result != result:
                print('test #{} failed!'.format(test_number))
                all_passed = False

    if all_passed:
        print('All tests passed!')
