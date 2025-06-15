month = input()
night_stay = int(input())
price_per_night = 0
studio_price = 0
apartment_price = 0
total_apartment_price = 0
total_studio_price = 0

if month == 'May' or month == 'October':
    if 7 < night_stay <= 14:
        studio_price = 50 * 0.95
        apartment_price = 65
    elif night_stay > 14:
        studio_price = 50 * 0.70
        apartment_price = 65 * 0.90
    else:
        studio_price = 50
        apartment_price = 65
    total_studio_price = night_stay * studio_price
    total_apartment_price = night_stay * apartment_price

elif month == 'June' or month == 'September':
    if night_stay <= 14:
        studio_price = 75.20
        apartment_price = 68.70
    elif night_stay > 14:
        studio_price = 75.20 * 0.80
        apartment_price = 68.70 * 0.90
    total_studio_price = night_stay * studio_price
    total_apartment_price = night_stay * apartment_price

elif month == 'July' or month == 'August':
    if night_stay <= 14:
        studio_price = 76
        apartment_price = 77
    elif night_stay > 14:
        studio_price = 76
        apartment_price = 77 * 0.90
    total_studio_price = night_stay * studio_price
    total_apartment_price = night_stay * apartment_price

print(f'Apartment: {total_apartment_price:.2f} lv.')
print(f'Studio: {total_studio_price:.2f} lv.')
