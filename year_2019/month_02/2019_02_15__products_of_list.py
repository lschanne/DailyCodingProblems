'''
February 15, 2019

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def productsOfList(inList):
    prod = 1
    for x in inList:
        prod *= x

    return [prod // x for x in inList]

def productsOfList_noDivision(inList):
    outList = [1 for x in inList]
    for idx, val in enumerate(inList):
        for jjj in range(len(outList)):
            if idx != jjj:
                outList[jjj] *= val
    return outList

if __name__ == '__main__':
    import sys
    inList = list(map(int, sys.argv[1:]))

    outList = productsOfList(inList)
    noDiv = productsOfList_noDivision(inList)
    same = noDiv == outList

    print('inList: {}'.format(inList))
    print('outList: {}'.format(outList))
    if same:
        print('The function without division returned the same output!')
    else:
        print('But the function without divison has a different result!')
        print('outList2: {}'.format(noDiv))