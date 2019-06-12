'''
June 3, 2019

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_root_to_leaf_paths(root):
    def _recurse(node, paths, current_path):
        if node is None:
            return paths

        current_path = current_path + [node.value]
        if (node.left is None) and (node.right is None):
            paths.append(current_path)
            return paths

        paths = _recurse(node.left, paths, current_path)
        paths = _recurse(node.right, paths, current_path)
        return paths

    return _recurse(root, [], [])

if __name__ == '__main__':
    test_cases = []

    # test 0
    tree = BinaryTree(
        1,
        BinaryTree(2),
        BinaryTree(
            3,
            BinaryTree(4),
            BinaryTree(5),
        )
    )
    result = [[1, 2], [1, 3, 4], [1, 3, 5]]
    test_cases.append([tree, result])

    # test 1
    tree = BinaryTree(0)
    result = [[0]]
    test_cases.append([tree, result])

    # test 2
    tree = BinaryTree(
        'a',
        BinaryTree('b'),
        BinaryTree('c'),
    )
    result = [['a', 'b'], ['a', 'c']]
    test_cases.append([tree, result])

    # idk there really aren't any edge cases for this.

    all_passed = True
    for idx, (tree, expected_result) in enumerate(test_cases):
        try:
            result = get_root_to_leaf_paths(tree)
        except Exception:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                print('expected: {}'.format(expected_result))
                print('actual:   {}'.format(result))
                all_passed = False
            else:
                print('test #{} passed!'.format(idx))
        print('--------------------------')
    if all_passed:
        print('All tests passed!')