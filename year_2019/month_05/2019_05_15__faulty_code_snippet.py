'''
May 15, 2019

What does the below code snippet print out? How can we fix the anonymous
functions to behave as we'd expect?

"""
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""
'''

# So the snippet as is will just print a bunch of 9's
# To "fix" the anonymous functions, we simply need to evaluate i at the time
# of function definition, and not at the time of execution
functions = [lambda i=i: i for i in range(10)]
for f in functions:
    print(f())
