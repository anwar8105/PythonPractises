# Problem Source : codingbat.com

'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''


def makes10(a, b):
    # true, either of them is equal to 10 or thier sum is equals to 10
    if (a == 10 or b == 10) or sum((a, b)) == 10:
        return True

    # false above condition fails
    return False


print(makes10(9, 10))  # true
print(makes10(9, 9))  # false
print(makes10(9, 1))  # true
