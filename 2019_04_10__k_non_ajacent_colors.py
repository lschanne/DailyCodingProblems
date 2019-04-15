'''
April 10, 2019

Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
'''

def can_be_done(adjacency_matrix, k):
    if not adjacency_matrix:
        return True

if __name__ == '__main__':
    for adjacency_matrix in (
        [],
        [
            [False, False, True],
            [False, False, True],
            [True, True, False],
        ],
    ):
        print(adjacency_matrix)
        for k in range(10):
            print('k={}: {}'.format(k, can_be_done(adjacency_matrix, k)))
        print('-------------------')
