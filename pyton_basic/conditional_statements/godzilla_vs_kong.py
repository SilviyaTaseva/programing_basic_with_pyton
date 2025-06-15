movie_budget = float(input())
extras_number = int(input())
outfit_extras_single_price = float(input())

outfit_extras_full_price = extras_number * outfit_extras_single_price
decor_price = movie_budget * 0.10

if extras_number >= 150:
    outfit_extras_full_price *= 0.90

full_movie_price = outfit_extras_full_price + decor_price

if movie_budget < full_movie_price:
    money_left = abs(movie_budget - full_movie_price)
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")
else:
    money_left = movie_budget - full_movie_price
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")


