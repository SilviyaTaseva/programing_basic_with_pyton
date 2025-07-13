lily_age = int(input())
wash_price = float(input())
toy_price = int(input())

money = 0
toy_count = 0
brother_money = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        money += (i // 2) * 10
        brother_money += 1
    else:
        toy_count += 1

money -= brother_money

total_toys = toy_price * toy_count
full_price = total_toys + money

if full_price >= wash_price:
    print(f'Yes! {full_price - wash_price:.2f}')
else:
    print(f'No! {wash_price - full_price:.2f}')

