# Problem Source : codingbat.com

'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''


def front_back(str):
    # swap, if str has two values
    if len(str) > 1:
        return str[-1:] + str[1:-1] + str[0]

    return str[:]  # won't swap if it has only one value


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print(front_back('anwar'))
