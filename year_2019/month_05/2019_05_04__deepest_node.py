'''
May 4, 2019

Given the root of a binary tree, return a deepest node. For example, in the
following tree, return d.

    a
   / \
  b   c
 /
d
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Yes, it also return the depth of the node
# I could write a helper function, but whatever
def get_deepest_node(node, depth=1, deepest_node=None, deepest_depth=0):
    if not node:
        return (deepest_node, deepest_depth)

    if depth > deepest_depth:
        print(node.value, depth, deepest_depth)
        deepest_depth = depth
        deepest_node = node

    if node.left:
        deepest_node, deepest_depth = get_deepest_node(
            node.left, depth + 1, deepest_node, deepest_depth
        )

    if node.right:
        deepest_node, deepest_depth = get_deepest_node(
            node.right, depth + 1, deepest_node, deepest_depth
        )

    return (deepest_node, deepest_depth)

if __name__ == '__main__':
    tree = BinaryTree(
        'a',
        BinaryTree('b', BinaryTree('d')),
        BinaryTree('c'),
    )
    print('deepest node: {}'.format(get_deepest_node(tree)[0].value))
