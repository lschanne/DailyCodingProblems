'''
April 4, 2019

Suppose an arithmetic expression is given as a binary tree. Each leaf is an
integer and each internal node is one of '+', '-', '*', or '/'.

Given the root ot such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   /  \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
'''

class BinaryArithmeticTree:
    def __init__(self, value, left_child=None, right_child=None):
        # It feels a little funny to even do input validation for something
        # that only I will use, but whatever... it's not even that good looking
        if not (
            isinstance(value, int) or
            isinstance(value, str) and (
                value.isdigit() or
                value in '+-*/'
            )
        ):
            raise ValueError(
                'Input value must be either an int or an arithmetic '
                'operator [+ - * /]! BinaryTree received "{}".'.format(value)
            )

        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def solve_binary_tree(tree):
    if not tree:
        return 0

    value = tree.value
    if isinstance(value, int) or value.isdigit():
        return int(tree.value)

    left = solve_binary_tree(tree.left_child)
    right = solve_binary_tree(tree.right_child)
    if value == '+':
        return left + right

    if value == '-':
        return left - right

    if value == '*':
        return left * right

    if value == '/':
        return left // right

    raise NotImplementedError

if __name__ == '__main__':
    bat = BinaryArithmeticTree(
        '*',
        left_child=BinaryArithmeticTree(
            '+',
            left_child=BinaryArithmeticTree(3),
            right_child=BinaryArithmeticTree(2)
        ),
        right_child=BinaryArithmeticTree(
            '+',
            left_child=BinaryArithmeticTree(4),
            right_child=BinaryArithmeticTree(5)
        ),
    )
    print(solve_binary_tree(bat))