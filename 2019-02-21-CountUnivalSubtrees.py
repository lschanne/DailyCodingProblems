'''
February 21, 2019

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

def univalTree(node):
    return _univalTree(node)[1]

def _univalTree(node):
    isUnival, univalCount = True, 0
    for subNode in (node.left, node.right):
        if subNode:
            subUnival, subCount = _univalTree(subNode)
            isUnival &= subUnival and node.value == subNode.value
            univalCount += subCount
    if isUnival:
        univalCount += 1
    return isUnival, univalCount

if __name__ == '__main__':
    class BinaryTree:
        def __init__(self, value=0, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    # the tree given as an example in the docstring
    root = BinaryTree(
        value=0,
        left=BinaryTree(value=1),
        right=BinaryTree(
           value=0,
           left=BinaryTree(
              value=1,
              left=BinaryTree(value=1),
              right=BinaryTree(value=1),
           ),
           right=BinaryTree(value=0),
        )
    )
    # should print 5 - it doesn't
    print(univalTree(root))

    # should print 1 - it does
    print(univalTree(BinaryTree()))

    # should print 3 - it does
    print(univalTree(BinaryTree(
       value=1,
       left=BinaryTree(value=1),
       right=BinaryTree(value=1),
    )))

    # should print 4 - it prints 5
    print(univalTree(BinaryTree(
       value=0,
       left=BinaryTree(
          value=1,
          left=BinaryTree(value=1),
          right=BinaryTree(value=1),
       ),
       right=BinaryTree(value=0),
    )))

    # should print 2
    print(univalTree(BinaryTree(
       value=0,
       left=BinaryTree(value=1),
       right=BinaryTree(value=0),
    )))