'''
February 14, 2019

Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

import argparse
import sys

class TwoNumberSumInList:
    def __init__(self, inputs=sys.argv[1:]):
        self.parseInputs(inputs)

    def main(self):
        self.result = self.twoNumberSumInList(
                numList=self.numList,
                k=self.k
        )
        self._displayResults()

    @staticmethod
    def twoNumberSumInList(numList, k):
        '''
        Typically, we expect set operations to perform in O(1), so this
        function operations in O(n), where n is the length of numList.

        On an empty list, we will return False. We handle negatives and
        zeroes just fine with this method.
        (i.e. twoNumberSumInList([0,0], 0) = True
              twoNumberSumInList([0], 0) = False
        )

        Not much more to say. I thought about including the two numbers found
        in the response, but that's not specified by the problem statement.
        '''
        numSet = set()
        for x in numList:
            if x in numSet:
                return True
            numSet.add(k - x)
        return False

    def parseInputs(self, inputs = sys.argv[1:]):
        parser = argparse.ArgumentParser()
        parser.add_argument(
                '-k', action='store', dest='k', default=17,
                help='The number to which any two numbers in the list should sum.'
        )
        parser.add_argument(
                '-l', '--list', action='store', dest='list', nargs='*',
                help='List of numbers to check. Separate numbers with a space.'
        )
        options, unknown_args = parser.parse_known_args(inputs)

        if options.list:
            options.list = list(map(int, options.list))
        else:
            options.list = [10, 15, 3, 7]

        self.numList = options.list
        self.k = int(options.k)

    def _displayResults(self):
        msg='''
            Given the following input list: {numList}
            And given the following value of k: {k:.0f}
            There {result} two numbers in the input list that
            sum to the value of k!
            '''.format(
                numList=self.numList,
                k=self.k,
                result='ARE' if self.result else 'ARE NOT'
        )
        print(msg)

if __name__ == '__main__':
    TwoNumberSumInList().main()
