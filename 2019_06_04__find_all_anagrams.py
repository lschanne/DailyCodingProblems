'''
June 4, 2019

Given a word W and a string S, find all starting indices in S which are
anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
'''

# I guess I'll say we're ignoring case
def find_all_anagrams(W, S):
    result = []
    chars_of_W = get_char_counts(W)
    for idx in range(1 + len(S) - len(W)):
        if get_char_counts(S[idx:idx + len(W)]) == chars_of_W:
            result.append(idx)
    return result

def get_char_counts(string):
    char_counts = {}
    for char in string.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

if __name__ == '__main__':
    import sys
    for idx in range(1, len(sys.argv), 2):
        W, S = sys.argv[idx:idx + 2]
        print('W: {}'.format(W))
        print('S: {}'.format(S))
        print('result: {}'.format(find_all_anagrams(W, S)))
        print('-----------------------')
