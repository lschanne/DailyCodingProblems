'''
March 21, 2019

Given the root to a binary search tree, find the second largest node in the
tree.

Note to self: "largest" is a bit ambiguous, but I'm assuming that "size" is the
count of children under the node.
'''

# So the second largest node obviously has to be either the left_child
# or the right_child of the root node
def get_second_largest_node(root_node):
    return max((root_node.left_child, root_node.right_child), key=get_children)

def get_children(node):
    # If the parent node is missing one of its children, you would still
    # prefer to return a child that has no children of its own
    if not node:
        return -1

    children = 0
    if node.left_child:
        children += 1 + get_children(node.left_child)
    if node.right_child:
        children += 1 + get_children(node.right_child)
    return children

class BinarySearchTree:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

if __name__ == '__main__':
    bst = BinarySearchTree(
        'A',
        BinarySearchTree('B'),
        BinarySearchTree(
            'C',
            BinarySearchTree('D'),
        ),
    )
    print(get_second_largest_node(bst).value)
