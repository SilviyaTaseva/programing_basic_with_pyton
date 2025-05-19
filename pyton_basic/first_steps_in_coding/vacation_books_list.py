book_pages = int(input( ))
pages_per_hour = int(input())
days = int(input())
total_hours = book_pages/pages_per_hour
hour_per_day = total_hours/days

print(round(hour_per_day))