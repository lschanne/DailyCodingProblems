'''
June 5, 2019

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree. Assume that each node in the tree also has a pointer to
its parent.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is
defined between two nodes v and w as the lowest node in T that has both v and w
as descendants (where we allow a node to be a descendant of itself)."
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.parent = None
        self.value = value
        self.left = left
        if left is not None:
            self.left.parent = self
        self.right = right
        if right is not None:
            self.right.parent = self

def find_lowest_common_ancestor(*args):
    if len(args) == 1:
        return args[0]

    node_parents = []
    current_nodes = list(args)
    check_node = [True for _ in range(len(args))]
    while True:
        if not any(check_node):
            return None
        for idx, node in enumerate(current_nodes):
            if not check_node[idx]:
                continue
            if node in node_parents:
                return node
            node_parents.append(node)
            if node.parent is None:
                check_node[idx] = False
            else:
                current_nodes[idx] = node.parent

if __name__ == '__main__':
    test_objects = []

    # test 0
    tree = BinaryTree(0)
    args = [tree]
    expected_result = tree
    test_objects.append([args, expected_result])

    # test 1
    tree = BinaryTree(0, BinaryTree(1), BinaryTree(2))
    args = [tree, tree.left, tree.right]
    expected_result = tree
    test_objects.append([args, expected_result])

    # test 2
    tree1 = BinaryTree(1)
    tree2 = BinaryTree(2)
    args = [tree1, tree2]
    expected_result = None
    test_objects.append([args, expected_result])

    # test 3
    tree = BinaryTree(0, BinaryTree(1, BinaryTree(2), BinaryTree(3)))
    args = [tree.left.left, tree.left.right]
    expected_result = tree.left
    test_objects.append([args, expected_result])

    # test 4
    args = []
    expected_result = None
    test_objects.append([args, expected_result])

    all_passed = True
    for idx, (args, expected_result) in enumerate(test_objects):
        try:
            result = find_lowest_common_ancestor(*args)
        except:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result == expected_result:
                print('test #{} passed!'.format(idx))
            else:
                print('test #{} failed!'.format(idx))
                all_passed = False
    if all_passed:
        print('All tests passed!')
