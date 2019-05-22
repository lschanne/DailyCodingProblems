'''
May 19, 2019

Given a number represented by a list of digits, find the next greater
permutation of a number, in terms of lexicographic ordering. If there is not
greater permutation possible, return the permutation with the lowest
value/ordering.

For example, the list [1,2,3] should return [1,3,2].
The list [1,3,2] should return [2,1,3].
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory
(disregarding the input memory)?
'''

# So this function will edit the input in-place, since they want the
# operation to execute without allocating extra memory
def next_highest_permutation_of_digits(current_permutation):
    # Assumaxg that these are digits (i.e. 0 <= x <= 9)
    max_value = -1
    max_idx = len(current_permutation)
    this_idx = max_idx - 1
    while this_idx >= 0:
        this_value = current_permutation[this_idx]
        if this_value < max_value:
            current_permutation[max_idx] = this_value
            current_permutation[this_idx] = max_value
            break
        max_value = this_value
        max_idx = this_idx
        this_idx -= 1

    # the digits to the right of the swap (this_idx) need to be sorted
    for idx1 in range(this_idx + 1, len(current_permutation) - 1):
        for idx2 in range(idx1 + 1, len(current_permutation)):
            if current_permutation[idx1] > current_permutation[idx2]:
                (current_permutation[idx1], current_permutation[idx2]) = (
                    current_permutation[idx2], current_permutation[idx1]
                )

    return current_permutation

if __name__ == '__main__':
    import sys
    current_permutation = [int(x) for x in sys.argv[1:]]
    for _ in range(10):
        print(''.join(map(str, current_permutation)))
        next_highest_permutation_of_digits(current_permutation)
