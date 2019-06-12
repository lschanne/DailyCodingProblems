'''
March 4, 2019

A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two neighboring
houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves
this goal.
'''

# So here is the brute force recursive technique
def get_min_cost_brute_force(
    cost_matrix,
    min_cost=None,
    cost=0,
    this_row=0,
    prev_k=None
):
    if this_row == len(cost_matrix):
        if min_cost is None or cost < min_cost:
            min_cost = cost
        return min_cost

    for k, val in enumerate(cost_matrix[this_row]):
        if k != prev_k:
            min_cost = get_min_cost_brute_force(
                cost_matrix,
                min_cost,
                cost + val,
                this_row + 1,
                k
            )

    return min_cost

# Surely we can do better (don't call me surely)...
# This is definitely better, but there's probably an even better solution
# Also my confidence that it works on every scenario is not extremely high
def get_min_cost(cost_matrix):
    min_cost = 0
    sorted_matrix = [
        list(sorted(enumerate(row), key=lambda (key, val): val))
        for row in cost_matrix
    ]

    prev_k = None
    for idx, sorted_row in enumerate(sorted_matrix):
        for sort_idx, (k, cost) in enumerate(sorted_row):
            if k == prev_k:
                continue

            if not (
                idx + 1 < len(sorted_matrix) and
                sorted_matrix[idx + 1][0][0] == k and
                sorted_matrix[idx + 1][0][1] + sorted_row[sort_idx + 1][1] <
                sorted_matrix[idx + 1][1][1] + cost
            ):
                break

        min_cost += cost
        prev_k = k

    return min_cost

if __name__ == '__main__':
    test_inputs = [
        {
            'input': [],
            'output': 0,
        },
        {
            'input': [
                [1, 2, 3],
                [3, 2, 1],
                [2, 1, 3],
            ],
            'output': 3,
        },
        {
            'input': [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
            ],
            'output': 1,
        },
        {
            'input': [
                [5, 2],
                [2, 1],
                [5, 2],
            ],
            'output': 6,
        },
        {
            'input': [
                [2, 2],
                [2, 1],
                [3, 2],
            ],
            'output': 6,
        },
        {
            'input': [
                [2, 2],
                [2, 1],
                [2, 2],
            ],
            'output': 5,
        },
        {
            'input': [
                [1, 5, 5],
                [1, 2, 3],
                [5, 1, 5],
            ],
            'output': 5,
        },
        {
            'input': [
                [3, 5, 7],
                [2, 0, 1],
            ],
            'output': 3,
        }
    ]

    all_passed = True
    for input_dict in test_inputs:
        output = get_min_cost(input_dict['input'])
        passed = output == input_dict['output']
        all_passed &= passed
        print('input: {}'.format(input_dict['input']))
        print('expected output: {}'.format(input_dict['output']))
        print('actual output: {}'.format(output))
        print('result: {}'.format('PASSED' if passed else 'FAILED'))
        print('----------------------------------------------')

    if all_passed:
        print('ALL TESTS PASSED.')
    else:
        print('NOT ALL TESTS PASSED.')
