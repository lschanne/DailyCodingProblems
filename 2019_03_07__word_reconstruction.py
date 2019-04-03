'''
March 7, 2019

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
'''

# To clarify, we are not returning all possible reconstructions, just any of
# them (if one exists)
def get_reconstruction(words, string, reconstruction=[]):
    if not string:
        return reconstruction

    for word in words:
        if string.startswith(word):
            result = get_reconstruction(
                words,
                string[len(word):],
                reconstruction + [word]
            )
            if result:
                return result

    # if no reconstruction exists, return None


if __name__ == '__main__':
    import sys
    string = sys.argv[1] if len(sys.argv) > 1 else ''
    words = sys.argv[2:]
    print('string: {}'.format(string))
    print('words: {}'.format(words))
    print('result: {}'.format(get_reconstruction(words, string)))

