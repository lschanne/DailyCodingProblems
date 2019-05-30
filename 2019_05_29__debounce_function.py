'''
May 29, 2019

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not
be called for N milliseconds.
'''

from datetime import datetime, timedelta

def debounce(N):
    def debounce_decorator(func):
        run_time = datetime.now() + timedelta(milliseconds=N)

        def debounced_func():
            if datetime.now() >= run_time:
                return func()

        return debounced_func
    return debounce_decorator

if __name__ == '__main__':
    @debounce(N=5000)
    def f():
        print('runtime: {}'.format(datetime.now()))
        return True

    print('start: {}'.format(datetime.now()))
    while True:
        if f():
            break
