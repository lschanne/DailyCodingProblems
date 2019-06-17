'''
June 14, 2019

Given a string which we can delete at most k, return whether you can make a
palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to
get 'waterretaw'.
'''

def k_deletions_to_palindrome(string, k=0):
    def _recurse(string, k):
        if string == string[::-1]:
            return True

        if k <= 0:
            return False

        for idx in range(len(string)):
            if _recurse(string[:idx] + string[idx + 1:], k - 1):
                return True

        return False

    return _recurse(string, k)

if __name__ == '__main__':
    import sys
    string, k = sys.argv[1:3]
    k = int(k)
    print('string: {}'.format(string))
    print('k: {}'.format(k))
    print('can be made a palindrome: {}'.format(
        k_deletions_to_palindrome(string, k))
    )
