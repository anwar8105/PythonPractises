# Problem Source : codingbat.com
'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''


def sleep_in(weekday, vacation):
    # weekday and vacation are True, return true
    if weekday and vacation:
        return True
        # weekday is false and vacation is true, return true
    elif not weekday or vacation:
        return True
    # if none, return false
    return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
