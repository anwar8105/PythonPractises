# Problem Source : codingbat.com
"""
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""


def make_abba(a, b):
    # concate method
    return a+b+b+a


# def make_abba(a, b):
    # f-strings method
#    return f"{a}{b}{b}{a}"


print(make_abba('hi', 'bye'))
print(make_abba('yo', 'alice'))
print(make_abba('what', 'up'))
