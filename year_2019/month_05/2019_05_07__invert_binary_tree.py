'''
May 7, 2019

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:
  a
 / \
 c  b
 \  / \
  f e  d
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = '[node {}'.format(self.value)
        if self.left:
            result += '; left={}'.format(self.left)
        if self.right:
            result += '; right={}'.format(self.right)
        result += ']'
        return result

def invert_binary_tree(tree):
    if tree is None:
        return tree

    tree.left, tree.right = (
        invert_binary_tree(tree.right),
        invert_binary_tree(tree.left)
    )

    return tree

if __name__ == '__main__':
    tree = BinaryTree(
        'a',
        BinaryTree(
            'b',
            BinaryTree('d'),
            BinaryTree('e'),
        ),
        BinaryTree(
            'c',
            BinaryTree('f')
        )
    )
    print('input tree: {}'.format(tree))
    print('output tree: {}'.format(invert_binary_tree(tree)))