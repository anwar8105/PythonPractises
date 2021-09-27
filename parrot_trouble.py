# Problem Source : codingbat.com

'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''


def parrot_trouble(talking, hour):
    # chech parrot is talking
    if talking:
        # hour before 7 or after 20
        if hour < 7 or hour > 20:
            # return true, that is we are in trouble
            return True
        else:
            # false if timing doesn't match
            return False

    # false if parrot is not talking
    return False


print(parrot_trouble(True, 6))  # true
print(parrot_trouble(True, 7))  # false
print(parrot_trouble(False, 6))  # false
print(parrot_trouble(True, 21))  # true
print(parrot_trouble(False, 21))  # false
