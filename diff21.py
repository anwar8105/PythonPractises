# Problem Source : codingbat.com
'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''


def diff21(n):
    var_21 = 21

    if n <= var_21:
        return abs(n - var_21)

    # if n greater than 21, return absolute differnce value * 2
    return abs(n - var_21) * 2


print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(22))
print(diff21(50))
