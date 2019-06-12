'''
April 29, 2019

Given an array of numbers, find the length of the longest increasing
subsequence in the array. The subsequence does not necessarily have to
be contiguous.

For example, given the array
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def get_longest_increasing_subsequence(sequence, idx=0, this_sequence=[]):
    if idx == len(sequence):
        return this_sequence

    results = [this_sequence]
    if not this_sequence or sequence[idx] > this_sequence[-1]:
        results.append(
            get_longest_increasing_subsequence(
                sequence, idx + 1, this_sequence + [sequence[idx]]
            )
        )

    results.append(
        get_longest_increasing_subsequence(
            sequence, idx + 1, this_sequence
        )
    )

    return max(results, key=len)

if __name__ == '__main__':
    import sys
    input_sequence = list(map(int, sys.argv[1:]))
    print('input sequence: {}'.format(input_sequence))
    print('longest increasing subsequence: {}'.format(
        get_longest_increasing_subsequence(input_sequence)
    ))