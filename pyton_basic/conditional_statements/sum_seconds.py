first_timer = int(input())
second_timer = int(input())
third_timer = int(input())

total_time = first_timer + second_timer + third_timer

minutes = total_time // 60
seconds = total_time % 60

if seconds< 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')