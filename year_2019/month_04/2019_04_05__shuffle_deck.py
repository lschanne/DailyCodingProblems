'''
April 5, 2019

Given a function that generates perfectly random numbers between 1 and k
(inclusive), where k is an input, write a function that shuffles a deck of
cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''

import copy
import numpy as np

# we'll use np.random.randint for our perfectly random number generator
DEFAULT_RANDOM_GENERATOR = lambda k: np.random.randint(1, k + 1)

def shuffle_deck(deck, random_generator=None):
    # random_generator should take one argument, k, to generator 
    # a random number between 1 and k, inclusive
    if random_generator is None:
        random_generator = DEFAULT_RANDOM_GENERATOR

    shuffled_deck = copy.deepcopy(deck)

    # employ a classic Fisher-Yates shuffle
    # I think that maintains equally likely permutations...
    # At the very least it's definitely O(N) and definitely a
    # random shuffle
    N = len(deck)
    for idx1 in range(N - 1, 0, -1):
        # it feels awkward to use a random number generator from 1..k
        # like you would rather just use 0..k, but maybe I'm missing the point
        idx2 = random_generator(idx1 + 1) - 1
        (shuffled_deck[idx1], shuffled_deck[idx2]) = (
                shuffled_deck[idx2], shuffled_deck[idx1]
        )

    return shuffled_deck


if __name__ == '__main__':
    import sys
    deck = sys.argv[1:]
    print('unshuffled deck: {}'.format(deck))
    for i in range(10):
        print('-------------------------------')
        print('Shuffle #{}: {}'.format(i + 1, shuffle_deck(deck)))

