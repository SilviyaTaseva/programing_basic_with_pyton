week_day = input()
ticket = 0


if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Friday' :
    ticket = 12
elif week_day == 'Wednesday' or week_day == 'Thursday' :
    ticket = 14
else:
    ticket = 16

print(ticket)