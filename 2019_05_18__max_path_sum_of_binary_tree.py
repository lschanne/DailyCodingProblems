'''
May 18, 2019

Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through
the root.
'''

# So the problem description is a bit confusing to me. Like are we supposed
# to specify a start and end node for the path? That doesn't seem right...
# I will implement a class method on my Tree class that searches all possible
# paths of length>=1 within that tree and returns the greatest sum of those
class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def max_path_sum(self):
        return self._max_path_sum(self)

    def _max_path_sum(self, current_sum=0):
        if current_sum > 0:
            current_sum += self.value
        else:
            current_sum = self.value

        possible_sums = [current_sum]
        for node in (self.left, self.right):
            if node is not None:
                if current_sum > 0:
                    node_sum = node._max_path_sum(current_sum)
                else:
                    node_sum = node._max_path_sum(0)

                possible_sums.append(node_sum)

        return max(possible_sums)

if __name__ == '__main__':
    test_cases = []

    # test 0
    tree = Tree(0)
    result = 0
    test_cases.append((tree, result))

    # test 1
    tree = Tree(-10)
    result = -10
    test_cases.append((tree, result))

    # test 2
    tree = Tree(5,
        left=Tree(-1,
            left=Tree(6),
        ),
        right=Tree(3),
    )
    result = 10
    test_cases.append((tree, result))

    all_passed = True
    for idx, (tree, expected_result) in enumerate(test_cases):
        try:
            result = tree.max_path_sum()
        except Exception:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                all_passed = False

    if all_passed:
        print('All tests passed!')
