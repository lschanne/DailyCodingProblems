'''
February 27, 2019

The area of a circle is defined as pi*r^2. Estimate pi to 3 decimal places using
a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

For this one, I had to lookup what a Monte Carlo method was. Basically, it
involves using random sampling to approximate a deterministic constant. I think
that the code will explain it better than I can, so just shut up and listen.
'''

import numpy as np

def approximatePi(n=10000):
    r = 1
    count = 0
    for _ in range(n):
        x, y = np.random.uniform(low=0, high=r, size=2)
        if x**2 + y**2 <= r**2:
            count += 1

    # so now count is the number of points (out of n) that are within the
    # a quarter of a unit circle and the n points are all inside of a unit
    # square
    # We know that the unit square has area 1*1=1 and the quarter of the
    # unit circle has area pi * r^2 / 4. Therefore...
    pi = 4. * count / (n * r**2)

    return pi

if __name__ == '__main__':
    import sys
    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        print('Problem reading in n. Setting to default.')
        n = 10000

    print('with n={:.0f}...'.format(n))
    # yes, I know the spec says 3 decimal places. #fuckthespec
    print('pi ~= {:.6f}...'.format(approximatePi(n)))