# Problem Source : codingbat.com

"""
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""


def non_start(a, b):
    '''
    we can join this extra code with if to find empty string
    elif not len(a) and not len(b):
        return '""'
    '''

    if len(a) > 0 and len(b) > 0:
        return a[1:] + b[1:]

    return a+b


print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))
print(non_start("", ""))
