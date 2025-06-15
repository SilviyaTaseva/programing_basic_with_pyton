stay_days = int(input())
room_type = input()
rating = input()

room_price = 0
total_price = 0

if room_type == 'room for one person':
    room_price = 18
elif room_type == 'apartment':
    room_price = 25
elif room_type == 'president apartment':
    room_price = 35

total_price = room_price * (stay_days-1)

if room_type == 'apartment':
    if stay_days < 10:
        total_price *= 0.7
    elif 10 <= stay_days < 15:
        total_price *= 0.65
    else:
        total_price *= 0.5
elif room_type == 'president apartment':
    if stay_days < 10:
        total_price *= 0.9
    elif 10 <= stay_days < 15:
        total_price *= 0.85
    else:
        total_price *= 0.8

if rating == 'positive':
    total_price *= 1.25
elif rating == 'negative':
    total_price *= 0.9
print(f'{total_price:.2f}')