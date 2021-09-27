# Problem Source : codingbat.com
'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''


def sum_double(a, b):
    # if a and b are equal, return (a+b) + (a+b)
    if a == b:
        return sum((a, b) + (a, b))

    # if both are not equal, return thier sum
    return sum((a, b))


print(sum_double(1, 2))
print(sum_double(2, 3))
print(sum_double(2, 2))
print(sum_double(3, 3))
