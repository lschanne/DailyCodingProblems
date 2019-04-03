'''
February 23, 2019

Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
'''

import datetime

def scheduler_v1(f, n):
    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).total_seconds() * 1000 < n:
        pass

    f()

import sched
import time

def scheduler(f, n):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(n / 1000., 1, f, ())
    s.run()

if __name__ == '__main__':
    import sys

    def f():
        print('xxxxx')

    for n in map(int, sys.argv[1:]):
        scheduler(f, n)