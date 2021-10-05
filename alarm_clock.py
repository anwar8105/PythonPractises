# Problem source: codingbat.com

'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00

reference 
0, s,
1, m
2, t
3, w,
4, t
5, f,
6, s

'''


def alarm_clock(day, vacation):
    if vacation:
        if day in range(1, 6):
            return '10:00'
        return 'off'    # day in [0, 6]:

    if day in range(1, 6):
        return '7:00'
    return '10:00'

    # return '7:00' if day in range(1, 6) else '10:00'


print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))

print(alarm_clock(6, True))
