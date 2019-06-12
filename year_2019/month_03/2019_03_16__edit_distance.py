'''
March 16, 2019

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between "kitten" and "sitting" is three:
substitute the "k" for "s", substitute the "e" for "i", and append a "g".

Given two strings, compute the edit distance between them.
'''

# I wonder if there's a better way to do this. I'm don't think that a non-naive
# approach will work.
def get_edit_distance(string_1, string_2, edit_distance=0):
    # Insertions for each remaining character
    if not string_1 or not string_2:
        return edit_distance + len(string_1) + len(string_2)

    # No change required
    if string_1[0] == string_2[0]:
        return get_edit_distance(string_1[1:], string_2[1:], edit_distance)

    # If the characters don't match, we can either insert, delete, or
    # substitute. Fortunately, inserting a character into one string can be
    # though to be the same as deleting a character from the other string
    # Similarly, for the purpose of calculating edit distance, it doesn't
    # matter which character gets substituted
    edit_distance += 1
    return min(
        # substitute one of the characters
        get_edit_distance(string_1[1:], string_2[1:], edit_distance),
        # insert into string_1 / delete from string_2
        get_edit_distance(string_1, string_2[1:], edit_distance),
        # insert into string_2 / delete from string_1
        get_edit_distance(string_1[1:], string_2, edit_distance),
    )

if __name__ == '__main__':
    import sys
    string_1, string_2 = sys.argv[1:3]
    print('string 1: {}'.format(string_1))
    print('string 2: {}'.format(string_2))
    print('edit distance: {}'.format(get_edit_distance(string_1, string_2)))
