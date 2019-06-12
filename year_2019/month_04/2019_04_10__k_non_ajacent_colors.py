'''
April 10, 2019

Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
'''

def can_be_done(adjacency_matrix, k):
    if k <= 0:
        return False

    colors = [None for _ in range(len(adjacency_matrix))]
    available_colors = [True for _ in range(k)]
    for iii, row in enumerate(adjacency_matrix):
        for kkk in range(k):
            available_colors[kkk] = True

        for jjj in range(iii):
            if row[jjj]:
                available_colors[colors[jjj]] = False

        for kkk in range(k):
            if available_colors[kkk]:
                colors[iii] = kkk
                break
        else:
            return False
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
