# Problem source :codingbat.com

'''
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''


def double_char(str):
    return ''.join(char * 2 for char in str)


'''
Same as
    result = ''
    for char in str:
        result += ''.join(char * 2)

    return result
'''


print(double_char('The'))
