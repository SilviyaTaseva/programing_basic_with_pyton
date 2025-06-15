group_budget = int(input())
season = input()
number_of_fishers = int(input())

price = 0
total_price = 0

if season == 'Spring':
    price = 3000
    if number_of_fishers <= 6:
        total_price = price * 0.9
    elif 7 <= number_of_fishers <= 11:
        total_price = price * 0.85
    elif number_of_fishers >= 12:
        total_price = price * 0.75
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if number_of_fishers <= 6:
        total_price = price * 0.9
    elif 7 <= number_of_fishers <= 11:
        total_price = price * 0.85
    elif number_of_fishers >= 12:
        total_price = price * 0.75
elif season == 'Winter':
    price = 2600
    if number_of_fishers <= 6:
        total_price = price * 0.9
    elif 7 <= number_of_fishers <= 11:
        total_price = price * 0.85
    elif number_of_fishers >= 12:
        total_price = price * 0.75
if number_of_fishers % 2 == 0 and season != 'Autumn':
    total_price = total_price * 0.95
else:
    total_price = total_price

if group_budget >= total_price:
    print(f'Yes! You have {group_budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - group_budget:.2f} leva.')

