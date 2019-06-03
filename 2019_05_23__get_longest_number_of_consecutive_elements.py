'''
May 23, 2019

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

def get_longest_number_of_consecutive_elements(integers):
    # the easy, obvious, not O(n) approach:
    max_count = 0
    count = 0
    prev = None
    for x in sorted(integers):
        if (prev is not None) and (x == prev + 1):
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
        prev = x
    return max_count

    # but how the friggin' frackin' way can we do this in O(n)?

if __name__ == '__main__':
    import sys
    integers = [int(x) for x in sys.argv[1:]]
    print('inputs: {}'.format(integers))
    print('output: {}'.format(
        get_longest_number_of_consecutive_elements(integers)
    ))
