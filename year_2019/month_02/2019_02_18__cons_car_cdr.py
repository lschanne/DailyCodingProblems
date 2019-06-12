'''
February 18, 2019

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.

This problem seems really simple and trivial to the point where I feel
like I'm missing something.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

if __name__ == '__main__':
    import sys
    a, b = map(int, sys.argv[1:])
    pair = cons(a, b)
    print(
        '''
        a: {a}, b: {b}
        car(pair): {car_out}
        cdr(pair): {cdr_out}
        '''.format(
            a=a,
            b=b,
            car_out=car(pair),
            cdr_out=cdr(pair),
        )
    )