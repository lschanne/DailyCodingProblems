'''
May 9, 2019

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
'''

# The wording is ambiguous here. Can we use mathematical operations and also
# use bit operations, or can we only use the bitwise OR operator? I don't
# actually think it's possible using ONLY the bitwise OR operator. Yes, we
# could use OR operators instead of AND operators in the second implementation,
# but you still need the negation and the NOT operator

# Here's a simple math operation implementation:
def x_if_b_else_y_USING_MATHEMTICAL_OPERATIONS(x, y, b):
    if b != 0 and b != 1:
        raise ValueError('b is expected to be 0 or 1.')
    return b * x + (1 - b) * y

# Here's a more complicated bitwise operation implementation:
def x_if_b_else_y(x, y, b):
    if b != 0 and b != 1:
        raise ValueError('b is expected to be 0 or 1.')
    return (x & -b) | (y & ~-b)

if __name__ == '__main__':
    import sys
    for i in range(1, len(sys.argv), 3):
        try:
            x, y, b = map(int, sys.argv[i:i + 3])
        except:
            continue
        print('x: {}, y: {}, b: {}'.format(x, y, b))
        try:
            print('result: {}'.format(x_if_b_else_y(x, y, b)))
        except ValueError:
            print('b is not 0 or 1!')
        print('----------------------------')
