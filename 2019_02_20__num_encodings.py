'''
February 20, 2019

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
'''

# Note that the actually decoding bit isn't required by the spec, but I think
# it's nice to have
def decode(x):
    return chr(int(x) + ord('a') - 1)

def numEncodings(message, count=0, decoding=''):
    if not message:
        print(decoding)
        return count + 1

    if message[0] == '0':
        return count

    count = numEncodings(message[1:], count, decoding + decode(message[0]))
    if 10 <= int(message[:2]) <= 26:
        count = numEncodings(message[2:], count, decoding + decode(message[:2]))

    return count

if __name__ == '__main__':
    import sys

    for x in sys.argv[1:]:
        y = numEncodings(x)
        print('numEncodings({}) = {:.0f}'.format(x, y))