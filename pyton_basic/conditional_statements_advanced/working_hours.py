working_hours = int(input())
working_day = input()

if working_hours >= 10 and working_hours <= 18 and (working_day == 'Monday'
or working_day == 'Tuesday' or working_day == 'Wednesday' or working_day == 'Thursday'
or working_day == 'Friday' or working_day == 'Saturday'):
    print('open')
else:
    print('closed')







