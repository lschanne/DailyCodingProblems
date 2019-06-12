'''
May 17, 2019

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
'''

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def copy(self):
        copy = Tree(self.value)
        if self.left is not None:
            copy.left = self.left.copy()
        if self.right is not None:
            copy.right = self.right.copy()
        return copy

    def __eq__(self, other):
        return (
            isinstance(other, Tree) and
            self.value == other.value and
            self.left == other.left and
            self.right == other.right
        )

# It's definitely a little funny to do this via a class, but I like having
# the `max_size` and `largest_bst` variables as pseudo-global variables
# available to the _get_largest_bst_subtree
class GetLargestBstSubtree:
    def get_largest_bst_subtree(self, node):
        self.max_size = 0
        self.largest_bst = None
        self._get_largest_bst_subtree(node)
        return (self.largest_bst, self.max_size)

    def _get_largest_bst_subtree(self, node):
        # Although None is not really a BST, we're returning None in the event
        # that no BST tree/subtree exists
        # Also, having this return True helps with the rest of the logic
        if node is None:
            return (True, 0)

        left_bst, left_size = self._get_largest_bst_subtree(node.left)
        right_bst, right_size = self._get_largest_bst_subtree(node.right)

        if (
            left_bst and right_bst and
            isinstance(node.value, int) and
            (
                node.left is None or (
                    isinstance(node.left.value, int) and
                    node.left.value <= node.value
                )
            ) and
            (
                node.right is None or (
                    isinstance(node.right.value, int) and
                    node.right.value >= node.value
                )
            )
        ):
            size = 1 + max((left_size, right_size))
            if size > self.max_size:
                self.max_size = size
                self.largest_bst = node

            return (True, size)

        return (False, 0)


if __name__ == '__main__':
    test_cases = []

    # test 0
    tree = Tree(0)
    largest_bst = tree
    max_size = 1
    test_cases.append([tree, (largest_bst, max_size)])

    # test 1
    tree = Tree('a', Tree('b'), Tree('c'))
    largest_bst = None
    max_size = 0
    test_cases.append([tree, (largest_bst, max_size)])

    # test 2
    tree = Tree(5,
        left=Tree(1,
            left=Tree(0),
            right=Tree(2,
                left=Tree(2),
                right=Tree(3,
                    right=Tree(10),
                ),
            ),
        ),
        right=Tree(1,
            left=Tree(0),
            right=Tree(2)
        ),
    )
    largest_bst = tree.left
    max_size = 4
    test_cases.append([tree, (largest_bst, max_size)])

    all_passed = True
    for idx, (input_tree, expected_result) in enumerate(test_cases):
        try:
            result = GetLargestBstSubtree().\
                get_largest_bst_subtree(input_tree)
        except Exception:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                all_passed = False

    if all_passed:
        print('All {} tests passed!'.format(len(test_cases)))