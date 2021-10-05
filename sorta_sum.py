# Problem source : codingbat.com

'''
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
'''


def sorta_sum(a, b):
    if a + b in range(10, 20):
        return 20

    return a + b    # sum((a,b)) is also fine

    # could be written as, return 20 if sum((a, b)) in range(10, 20) else sum((a, b))


print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))
