
flower_kind = input()
flower_amount = int(input())
budget = int(input())
flower_price = 0
total_price = 0

if flower_kind == 'Roses':
    flower_price = 5
    if flower_amount > 80:
        total_price = flower_amount * flower_price * 0.9
    else:
        total_price = flower_amount * flower_price
elif flower_kind == 'Dahlias':
    flower_price = 3.80
    if flower_amount > 90:
        total_price = flower_amount * flower_price * 0.85
    else:
        total_price = flower_amount * flower_price
elif flower_kind == 'Tulips':
    flower_price = 2.80
    if flower_amount > 80:
        total_price = flower_amount * flower_price * 0.85
    else:
        total_price = flower_amount * flower_price
elif flower_kind == 'Narcissus':
    flower_price = 3
    if flower_amount < 120:
        total_price = flower_amount * flower_price * 1.15
    else:
        total_price = flower_amount * flower_price
elif flower_kind == 'Gladiolus':
    flower_price = 2.50
    if flower_amount < 80:
        total_price = flower_amount * flower_price * 1.20
    else:
        total_price = flower_amount * flower_price

if total_price <= budget:
    left_money = budget - total_price
    print(f'Hey, you have a great garden with {flower_amount} {flower_kind} and {left_money:.2f} leva left.')
else:
    needed_money = total_price - budget
    print(f'Not enough money, you need {needed_money:.2f} leva more.')