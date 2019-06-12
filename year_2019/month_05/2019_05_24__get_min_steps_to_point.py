'''
May 24, 2019

You are in an infinite 2D grid where you can move in any of the 8 directions:
  (x, y) to
    (x + 1, y),
    (x - 1, y),
    (x, y + 1),
    (x, y - 1),
    (x - 1, y - 1),
    (x + 1, y + 1),
    (x - 1, y + 1),
    (x + 1, y - 1)
You are given a sequence of points and the order in which you need to cover the
points. Give the minimum number of steps in which you can achieve it. You start
from the first point.

Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move
from (1, 1) to (1, 2).
'''

def get_min_steps_to_point(points):
    steps = 0
    if not points:
        return steps

    prev_point = points[0]
    for next_point in points[1:]:
        steps += max(map(lambda i: abs(next_point[i] - prev_point[i]), (0, 1)))
        prev_point = next_point

    return steps

if __name__ == '__main__':
    test_cases = []

    # test 0
    test_cases.append(
        (
            [
                (0, 0),
                (1, 1),
                (1, 2)
            ],
            2
        )
    )

    # test 1
    test_cases.append(
        (
            [],
            0
        )
    )

    # test 2
    test_cases.append(
        (
            [
                (0, 0),
                (0, 0),
                (0, 0),
                (0, 0),
                (0, 0)
            ],
            0
        )
    )

    # test 3
    test_cases.append(
        (
            [
                (0, 0),
                (10, -15), # delta: (10, 15) => 15
                (2, 3), # delta: (8, 18) => 18
                (10, -15), # delta: (8, 18) => 18
                (5, 6) # delta: (5, 21) => 21
            ],
            15 + 18 + 18 + 21
        )
    )

    all_passed = True
    for idx, (test_input, expected_result) in enumerate(test_cases):
        try:
            result = get_min_steps_to_point(test_input)
        except Exception:
            print('test #{} raised an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                all_passed = False

    if all_passed:
        print('All tests passed!')
