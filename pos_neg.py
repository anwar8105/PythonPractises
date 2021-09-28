# Problem Source : codingbat.com
'''
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''


def pos_neg(a, b, negative):
    # check is negative set to true or false
    if negative:
        # if yes, both a and b should be negative numbers
        return (a < 0 and b < 0)
    else:
        # if not, either of them should be negative number
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-41, -5, True))
