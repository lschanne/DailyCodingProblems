'''
June 2, 2019

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd
bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
'''

'''
Explanation: (so that I understand what I did if I ever look at this again)
x:    x1 x2 x3 x4 x5 x6 x7 x8
x*2:  x2 x3 x4 x5 x6 x7 x8 0
x//2: 0  x1 x2 x3 x4 x5 x6 x7
So we mask x*2 with 10101010 (170)
And we mask x//2 with 01010101 (85)
Then we OR their respective bits
The mod255 at the end is to keep the result to an "8-bit integer"
'''
def even_odd_bit_swap(x):
    return ((x * 2) & 170) | ((x // 2) & 85)

if __name__ == '__main__':
    import sys
    for x in map(int, sys.argv[1:]):
        print('input: {}'.format(x))
        print('{:08b} ->'.format(x))
        print('{:08b}'.format(even_odd_bit_swap(x)))
        print('---------------------------')
