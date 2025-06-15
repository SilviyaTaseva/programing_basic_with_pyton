city = input()
sales_volume = float(input())
comission = 0

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        comission = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        comission = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        comission = sales_volume * 0.08
    elif sales_volume > 10000:
        comission = sales_volume * 0.12
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        comission = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        comission = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        comission = sales_volume * 0.10
    elif sales_volume > 10000:
        comission = sales_volume * 0.13
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        comission = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        comission = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        comission = sales_volume * 0.12
    elif sales_volume > 10000:
        comission = sales_volume * 0.145

if comission > 0:
    print(f'{comission:.2f}')
else:
    print('error')