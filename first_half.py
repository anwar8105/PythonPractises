# Problem Source : codingbat.com
"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""


def first_half(str):
    # Could be written as,
    # return str[0:round(len(str)/2)] if len(str) % 2 == 0 else None
    # But readability counts
    if len(str) % 2 == 0:
        return str[0:round(len(str) / 2)]

    return 'Not even'


print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
print(first_half('anwarnadaf'))
print(first_half('iloveyo'))
