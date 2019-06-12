'''
April 17, 2019

Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going left-to-right,
or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost
column. Similarly, given the target word 'MASS', you should return true,
since it's the last row.
'''

# We'll say that this search is case insensitive
def word_in_matrix(word, matrix):
    if not word:
        return True

    if (
        matrix and matrix[0] and
        (len(matrix) >= len(word) or len(matrix[0]) >= len(word))
    ):
        if (
            matrix[0][0].lower() == word[0].lower() and
            any((
                word_in_matrix(word[1:], matrix[1:]),
                word_in_matrix(word[1:], [row[1:] for row in matrix]),
            ))
        ) or (
            any((
                word_in_matrix(word, matrix[1:]),
                word_in_matrix(word, [row[1:] for row in matrix]),
            ))
        ):
            return True

    return False

if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    words = ['FOAM', 'MASS', 'SOAP', 'PLAYA', 'foam', 'soap', 'fOaM', 'sOaP']
    for word in words:
        print('word: {}'.format(word))
        print('is in matrix: {}'.format(word_in_matrix(word, matrix)))
