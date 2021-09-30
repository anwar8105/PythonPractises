# Problem Source : codingbat.com

'''
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
'''


def left(str):
    if len(str) > 2:
        return str[2:] + str[:2]

    return str
    # return str[2:] + str[:2], one line solution


print(left('hello'))
print(left('java'))
print(left('hi'))
print(left('anwar'))
print(left('h'))
