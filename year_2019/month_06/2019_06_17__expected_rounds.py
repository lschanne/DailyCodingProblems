'''
June 17, 2019

You have n fair coins and you flip them all at the same time. Any that come up
tails you set aside. The ones that come up heads you flip again. How many
rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to
play until one coin remains.
'''

# This is not even a programming question. This is just a question in
# probability...
def expected_rounds(n):
    return 2 * (n - 1)
