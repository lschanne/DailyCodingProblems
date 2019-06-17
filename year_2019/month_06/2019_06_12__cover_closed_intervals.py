'''
June 12, 2019

Given a set of closed intervals, find the smallest set of numbers that covers
all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
numbers that covers all these intervals is {3, 6}.
'''

def cover_closed_intervals(intervals):
    if not intervals:
        return (None, None)

    largest_start = None
    smallest_end = None
    for start, end in intervals:
        if largest_start is None or start > largest_start:
            largest_start = start
        if smallest_end is None or end < smallest_end:
            smallest_end = end

    return (min((largest_start, smallest_end)), largest_start)

if __name__ == '__main__':
    test_cases = []

    intervals = ()
    result = (None, None)
    test_cases.append([intervals, result])

    intervals = (
        [0, 3],
    )
    result = (0, 0)
    test_cases.append([intervals, result])

    intervals = (
        [0, 3],
        [2, 6],
    )
    result = (2, 2)
    test_cases.append([intervals, result])

    intervals = (
        [0, 3],
        [2, 6],
        [3, 4],
    )
    result = (3, 3)
    test_cases.append([intervals, result])

    intervals = (
        [0, 3],
        [2, 6],
        [3, 4],
        [6, 9],
    )
    result = (3, 6)
    test_cases.append([intervals, result])

    for intervals, expected_result in test_cases:
        result = cover_closed_intervals(intervals)
        if result != expected_result:
            raise ValueError(
                'intervals: {}\nexpected_result: {}\nresult: {}'.format(
                    intervals, expected_result, result
                )
            )
    print('all tests passed')
