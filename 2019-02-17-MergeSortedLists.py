'''
February 17, 2019

Return a new sorted merged list from K sorted lists, each with size N.

Example:
    mergeSortedLists([[10, 15, 30], [12, 15, 20], [17, 20, 32]]) =
        [10, 12, 15, 15, 17, 20, 20, 30, 32]

To call this script from the command line, separate items in list via commas.
Separate lists via spaces.

i.e. `python MergeSortedLists.py 10,15,30 12,15,20 17,20,32` will
      perform the call in the example above.

I'm going to add a requirement that any command line calls will be passing in
integers. Having to handle multiple types is more effort than I care to deal
with. However, if the function is imported and called with custom lists,
it should work as long as the items in the lists can be compared.
'''

import bisect
import sys

def mergeSortedLists(inLists):
    # Create a heap with a two-pair tuple:
    # - The index of the list within inLists
    # - The current index within that list
    heap = [(iii, 0) for iii,x in enumerate(inLists) if x]
    heap.sort(key=lambda pair: inLists[pair[0]][pair[1]])

    output = []
    while heap:
        iii,jjj = heap.pop(0)
        output.append(inLists[iii][jjj])

        # Increment the current index of the list
        # If the list has not been completely iterated through,
        # place it back into the heap such that the heap remains sorted
        jjj += 1
        if jjj < len(inLists[iii]):
            lo, hi = 0, len(heap)
            while lo < hi:
                mid = (lo + hi)//2
                mid_iii, mid_jjj = heap[mid]
                if inLists[iii][jjj] < inLists[mid_iii][mid_jjj]:
                    hi = mid
                else:
                    lo = mid + 1
            heap.insert(lo, (iii, jjj))

    return output

def verifyInputs(inputs = None):
    if inputs is None:
        inputs = getInputsFromCommandLine()

    # I guess you could throw an error if the lists aren't all sorted,
    # but we'll just sort them and pass them through
    inputs = [list(sorted(x)) for x in inputs]

    # Technically, the spec dicatates that all of the input lists will be the
    # same size, but the function doesn't require it, so we won't bother
    # verifying that

    return inputs

def getInputsFromCommandLine():
    return [map(int, x.split(',')) for x in sys.argv[1:]]

if __name__ == '__main__':
    inputs = verifyInputs()
    print('The input is:\n{}'.format(inputs))
    print('Calculating output...')
    output = mergeSortedLists(inputs)
    print('The output is:\n{}'.format(output))
