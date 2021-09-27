# Problem Source : Codingbat.com
'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''


def monkey_trouble(a_smile, b_smile):
    # if both are true or if both are not true, return true cause we are in trouble
    if a_smile and b_smile or not a_smile and not b_smile:
        return True

    # if either of them is smiling, return false
    return False


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
