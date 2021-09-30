# Problem Source : codingbat.com

"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""


def without_end(str):
    # Could be done like this but for readability it isn't good practise
    # return str[1:-1] if len(str) > 2 else ""

    # For readability this is good
    if len(str) <= 2:
        return ""

    return str[1:-1]


print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))
print(without_end('python'))
print(without_end('pythonprogrammer'))
