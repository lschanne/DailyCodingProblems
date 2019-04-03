'''
March 9, 2019

Implement locking in a binary tree. A binary tree node can be locked or
unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:
- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should
  return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should
  return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would
like. You may assume the class is used in a single-threaded program, so there
is no need for actual locks or mutexes. Each method should run in O(h), where
h is the height of the tree.
'''

'''
I don't care for the phrasing of this problem as I feel there is a bit of
ambiguity. However, I believe that I have more or less solved it as intended.
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.parent = None
        self.left = left
        self.right = right
        self.is_locked = False
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    @property
    def can_be_toggled(self):
        return (
            self._can_be_toggled_parent_traverse() and
            self._can_be_toggled_child_traverse()
        )

    def _can_be_toggled_parent_traverse(self):
        return (
            not self.parent or
            (
                not self.parent.is_locked and
                self.parent._can_be_toggled_parent_traverse()
            )
        )

    def _can_be_toggled_child_traverse(self):
        if self.left:
            if (
                self.left.is_locked or
                not self.left._can_be_toggled_child_traverse
            ):
                return False

        if self.right:
            if (
                self.right.is_locked or
                not self.right._can_be_toggled_child_traverse
            ):
                return False

        return True

    def lock(self):
        result = self.can_be_toggled
        if result:
            self.is_locked = True
        return result

    def unlock(self):
        result = self.can_be_toggled
        if result:
            self.is_locked = False
        return result

    def __str__(self):
        return 'BinaryTree: (data: {}, is_locked: {})'.format(
            self.data,
            self.is_locked
        )

if __name__ == '__main__':
    tree = BinaryTree(
        data=0,
        left=BinaryTree(1),
        right=BinaryTree(2)
    )
    print(tree.lock()) # True
    print(tree.is_locked) # True
    print(tree.unlock()) # True

    tree.left.lock()
    print(tree.lock()) # False
    print(tree.is_locked) # False
    print(tree.unlock()) # False

    print(tree.left.is_locked) # True
    print(tree.left.unlock()) # True
    print(tree.lock()) # True

    print(tree.left.lock()) # False
    print(tree.left.is_locked) # False
    print(tree.left.unlock()) # False
