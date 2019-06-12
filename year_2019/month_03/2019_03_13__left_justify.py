'''
March 13, 2019

Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully
justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed
as equally as possible, with the extra spaces, if any, distributed starting
from the left.

If you can only fit one word on a line, then you should pad the right-hand side
with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16,
you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def left_justify(k, words):
    result = []
    this_line = []
    line_length = 0
    for word in words:
        word_length = len(word)
        if word_length > k:
            raise ValueError(
                '"{}" is of greater length than than k ({})!'.format(
                    word,
                    k
                )
            )

        if word_length + line_length <= k:
            this_line.append(word)
            # Add an extra one for the space between this word and the next
            line_length += word_length + 1
        else:
            # the last word will of course not have a space
            line_length -= 1
            result.append(format_line(k, this_line, line_length))
            this_line = [word]
            line_length = word_length

    if this_line:
        result.append(format_line(k, this_line, line_length))

    return result

def format_line(k, line, line_length):
    num_words = len(line)
    # because a single word line is a special little snowflake
    if num_words == 1:
        return line[0].ljust(k)

    result = ''
    extra_spaces = k - line_length
    # the last word doesn't have any spaces after it
    space_inc = extra_spaces // (num_words - 1)
    if space_inc:
        extra_spaces %= space_inc

    # +1 for the standard space between words
    space_inc += 1
    for word in line:
        word += ' ' * space_inc
        if extra_spaces:
            word += ' '
            extra_spaces -= 1
        result += word

    # the last word doesn't have any spaces after it
    return result.strip()

if __name__ == '__main__':
    import sys
    k = int(sys.argv[1])
    words = sys.argv[2:]
    result = left_justify(k, words)
    for line in result:
        print(line)
