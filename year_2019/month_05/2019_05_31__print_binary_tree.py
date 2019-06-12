'''
May 31, 2019

Print the nodes in a binary tree level-wise. For example, the following should
print "1, 2, 3, 4, 5":
  1
 / \
2   3
   / \
  4   5
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        string = str(self.value)
        if self.left:
            string += ', {}'.format(self.left)
        if self.right:
            string += ', {}'.format(self.right)
        return string

if __name__ == '__main__':
    print(
        str(
            BinaryTree(
                1,
                BinaryTree(2),
                BinaryTree(
                    3,
                    BinaryTree(4),
                    BinaryTree(5),
                )
            )
        )
    )
