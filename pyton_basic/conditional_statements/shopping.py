peters_budget = float(input())
number_of_video_cards = int(input())
number_of_procesors = int(input())
number_of_ram = int(input())

video_card_price = 250
video_card_total = number_of_video_cards * video_card_price
procesors_price = number_of_procesors * (video_card_total * 0.35)
ram_price = number_of_ram * (video_card_total * 0.10)

total_price_for_all = video_card_total + procesors_price + ram_price

if number_of_video_cards > number_of_procesors:
    total_price_for_all *= 0.85

if peters_budget >= total_price_for_all:
    remaining_budget = peters_budget - total_price_for_all
    print(f"You have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_price_for_all - peters_budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")