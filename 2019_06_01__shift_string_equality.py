'''
June 1, 2019

Given two strings A and B, return whether or not A can be shifted some number
of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is
acb, return false.
'''

def shift_string_equality(A, B):
    if not (A or B):
        return not (A and B)

    for idx, char in enumerate(B):
        if (
            char == A[0] and
            A == (B[idx:] + B[:idx])
        ):
            return True
    return False

if __name__ == '__main__':
    import sys
    for idx in range(1, len(sys.argv), 2):
        A, B = sys.argv[idx:idx + 2]
        print('A: {}'.format(A))
        print('B: {}'.format(B))
        print('result: {}'.format(shift_string_equality(A, B)))
        print('-------------------')
