'''
March 14, 2019

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''

class RunLengthEncoder:
    def __init__(self):
        pass

    @classmethod
    def encode(cls, string):
        if not string:
            return ''

        encoded_string = ''
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                encoded_string += str(count) + prev_char
                prev_char = char
                count = 1

        encoded_string += str(count) + char
        return encoded_string

    @classmethod
    def decode(cls, string):
        if not string:
            return ''

        decoded_string = ''
        count_str = ''
        for char in string:
            if char.isdigit():
                count_str += char
            else:
                decoded_string += char * int(count_str)
                count_str = ''

        return decoded_string

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser_group = parser.add_argument_group()
    parser_group.add_argument(
        '--encode', '-e', action='store', dest='encode', default=None,
        help='Pass in a string to encode with run-length encoding.'
    )
    parser_group.add_argument(
        '--decode', '-d', action='store', dest='decode', default=None,
        help='Pass in a string to decode with run-length encoding.'
    )
    options = parser.parse_args()

    if options.encode:
        print('string to encode: {}'.format(options.encode))
        print('encoded string: {}'.format(
            RunLengthEncoder.encode(options.encode)
        ))

    if options.decode:
        print('string to decode: {}'.format(options.decode))
        print('decoded string: {}'.format(
            RunLengthEncoder.decode(options.decode)
        ))
