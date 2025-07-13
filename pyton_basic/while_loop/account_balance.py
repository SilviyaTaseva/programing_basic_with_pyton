money_total = 0

while True:
    comand = input()

    if comand == 'NoMoreMoney':
        break

    money_add = float(comand)

    if money_add < 0:
        print('Invalid operation!')
        break

    money_total += money_add
    print(f'Increase: {money_add:.2f}')

print(f'Total: {money_total:.2f}')