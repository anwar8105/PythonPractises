# Problem Source : codingbat.com
'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''


def near_hundred(n):
    return n in range(90, 111) or n in range(190, 211)


print(near_hundred(93))  # true
print(near_hundred(90))  # true
print(near_hundred(89))  # false
print(near_hundred(209))  # true
print(near_hundred(-101))  # false
