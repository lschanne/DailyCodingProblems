'''
February 26, 2019

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
'''

def getSubstring(s, k):
    result = []
    current = []
    chars = {}
    count = 0
    for c in s:
        current.append(c)
        chars[c] = chars.get(c, 0) + 1
        if chars[c] == 1:
            count += 1
        while count > k:
            c = current.pop(0)
            chars[c] -= 1
            if not chars[c]:
                count -= 1
        if count == k and len(current) > len(result):
            # need a deep copy
            result = current[:]

    return ''.join(result)

if __name__ == '__main__':
    import sys
    s, k = sys.argv[1:3]
    print('s: `{}`'.format(s))
    print('k: {}'.format(k))
    r = getSubstring(s, int(k))
    print('result: `{}`'.format(r))