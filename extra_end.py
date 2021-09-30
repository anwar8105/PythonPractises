# Problem Source : codingbat.com

"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""


def extra_end(str):
    if len(str) >= 2:
        return str[-2:]*2


# def extra_end(str):
#     # method 2
#     return str[-2:]*3 if len(str) >= 2 else None


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('hi'))
print(extra_end('candy'))
print(extra_end('code'))
