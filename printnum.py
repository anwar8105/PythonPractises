# Goal : print num input in sequence
# example : if input is 5, result should be 12345

def printNum(num):
    for i in range(num):
        print(i+1, end='')

printNum(5)