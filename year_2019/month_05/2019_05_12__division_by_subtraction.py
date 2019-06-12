'''
May 12, 2019

Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
'''

# This will break and/or not return correct results for negative numbers,
# but that's in accordance with the problem statement
def division_by_subtraction(numerator, divisor):
    quotient = 0
    while numerator >= divisor:
        numerator -= divisor
        quotient += 1
    return quotient

if __name__ == '__main__':
    import sys
    for idx in range(1, len(sys.argv), 2):
        num, div = map(int, sys.argv[idx: idx + 2])
        print('{} // {} = {}'.format(
            num, div, division_by_subtraction(num, div)
        ))
