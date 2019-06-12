'''
February 16, 2019

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        # assuming self.val is either a str or an int/float
        if isinstance(self.val, str):
            val = '"{}"'.format(self.val)
        else:
            val = str(self.val)

        left = self.left.serialize() if self.left else 'None'
        right = self.right.serialize() if self.right else 'None'

        return 'Node({}, left={}, right={})'.format(val, left, right)

    @staticmethod
    def deserialize(serialized_node):
        return eval(serialized_node)

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(node.serialize())
    print(Node.deserialize(node.serialize()).left.left.val)
    assert Node.deserialize(node.serialize()).left.left.val == 'left.left'
