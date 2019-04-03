'''
February 28, 2019

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.

Disclaimer: I didn't come up with this. DailyCodingProblems sent an email a few
weeks later with a how-to on solving this exact problem.
'''
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

if __name__ == '__main__':
    import sys
    print(pick(sys.argv[1:]))
