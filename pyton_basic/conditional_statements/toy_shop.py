tour_price = float(input())
number_of_puzzles = int(input())
number_of_speaking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_kids_trucks = int(input())
number_of_toys = (number_of_puzzles + number_of_speaking_dolls +
                  number_of_teddy_bears + number_of_minions+ number_of_kids_trucks)

puzzles = number_of_puzzles * 2.60
speaking_dolls = number_of_speaking_dolls * 3
teddy_bears = number_of_teddy_bears * 4.10
minions = number_of_minions * 8.20
kids_trucks = number_of_kids_trucks * 2


customer_order = puzzles + speaking_dolls + teddy_bears + minions + kids_trucks


if number_of_toys >= 50:
    customer_order *= 0.75

shop_rent = customer_order * 0.10
end_profit = customer_order - shop_rent

if end_profit >= tour_price:
    print(f"Yes! {end_profit - tour_price:.2f} lv left.")
else:
    needed_money = tour_price - end_profit
    print(f"Not enough money! {needed_money:.2f} lv needed.")














