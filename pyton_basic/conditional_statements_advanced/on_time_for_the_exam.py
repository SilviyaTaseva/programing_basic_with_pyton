exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute
time_difference = arrival_time_in_minutes - exam_time_in_minutes

if time_difference > 0:
    print('Late')
    hours = time_difference // 60
    minutes = time_difference % 60
    if hours > 0:
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif time_difference < -30:
    print('Early')
    time_difference = abs(time_difference)
    hours = time_difference // 60
    minutes = time_difference % 60
    if hours > 0:
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{minutes} minutes before the start')
else:
    print('On time')
    time_difference = abs(time_difference)
    hours = time_difference // 60
    minutes = time_difference % 60
    if hours > 0:
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{minutes} minutes before the start')
