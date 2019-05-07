'''
May 6, 2019

Using a read7() method that returns 7 characters from a file, implement
readN(n) which reads n characters.

For example, given a file with the content "Hello world", three read7()
returns "Hello w", "orld" and then "".
'''

LEN = 7
FILE_INDEX = {}

def read7(fh):
    idx = FILE_INDEX.get(fh, 0)
    with open(fh, 'r') as f:
        result = f.read()[idx: idx + LEN]

    FILE_INDEX[fh] = idx + LEN
    return result

def readN(fh, n=LEN):
    quotient = n // LEN
    remainder = n % LEN
    if remainder:
        quotient += 1

    result = ''
    for _ in range(quotient):
        next_read = read7(fh)
        if not next_read:
            break
        result += next_read

    extra = len(result) - n
    if extra > 0:
        result = result[:-extra]
        FILE_INDEX[fh] -= extra

    return result

if __name__ == '__main__':
    import sys
    for idx in range(1, len(sys.argv), 2):
        fh = sys.argv[idx]
        n = int(sys.argv[idx + 1])
        print('fh: {}; n: {}'.format(fh, n))
        print('ouput: {}'.format(readN(fh, n)))
        print('----------------------------------')