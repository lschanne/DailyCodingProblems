'''
March 25, 2019

Given an array of integers where every integer occurs three times except for
one integer, which only occurs once, find and return the non-duplicated
integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

# So obviously this question is quite easy without the O(1) space constraint
def get_single_occurrence_unconstrained_space(inputs):
    counts = {}
    for x in inputs:
        counts[x] = counts.get(x, 0) + 1

    for x, count in counts.items():
        if count == 1:
            return x

# Or without the O(N) time constraint
def get_single_occurrence_unconstrained_time(inputs):
    inputs.sort()
    result = None
    new = False
    for x in inputs:
        if x != result:
            if new:
                return result
            new = True
        else:
            new = False

        result = x


# But I'm at a loss for how to do it with both of those constraints...
def get_single_occurrence(inputs):
    pass

if __name__ == '__main__':
    import sys
    inputs = list(map(int, sys.argv[1:]))
    print('inputs: {}'.format(inputs))
    print('result: {}'.format(get_single_occurrence(inputs)))
