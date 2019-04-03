'''
February 22, 2019

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def nonAdjacentSum_take1(numbers):
    '''
    This is wrong for something like [5, 6, 5].
    Also, it isn't O(N) or constant space.
    '''
    inUse = [False for _ in range(len(numbers))]
    result = 0
    for idx, val in sorted(
        enumerate(numbers), key=lambda x: x[1], reverse=True
    ):
        if val <= 0:
            break

        if (
            (idx == 0 or not inUse[idx - 1]) and
            (idx == len(numbers) - 1 or not inUse[idx + 1])
        ):
            result += val
            inUse[idx] = True

    return result

def nonAdjacentSum(numbers):
    '''
    Well this is pretty good. It's a bit ugly and I think that big conditional
    could be better, but it fits the spec. I can't think of any cases that
    would break this function.
    '''
    result = 0
    idx = 0
    N = len(numbers)
    while idx <= N:
        idx += 1
        val = numbers[idx - 1]
        if (
            idx < N and
            numbers[idx] > 0 and
            (
                (
                    idx + 1 < N and
                    numbers[idx] > val + numbers[idx + 1]
                ) or
                (
                    idx + 1 == N and
                    numbers[idx] > val
                )
            )
        ):
            val = numbers[idx]
            idx += 1
        if val > 0:
            idx += 1
            result += val

    return result

if __name__ == '__main__':
    import sys
    numbers = list(map(int, sys.argv[1:]))
    result = nonAdjacentSum(numbers)
    print('input numbers: {}'.format(numbers))
    print('result: {:.0f}'.format(result))