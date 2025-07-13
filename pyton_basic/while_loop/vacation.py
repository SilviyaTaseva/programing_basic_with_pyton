money_needed = float(input())
money_available = float(input())
day_counter = 0
spend_days = 0

while money_available < money_needed and spend_days < 5:
    action = input()
    money_counter = float(input())

    if action == 'save':
        money_available += money_counter
        spend_days = 0
    elif action == 'spend':
        money_available -= money_counter
        spend_days += 1
        if money_available < 0:
            money_available = 0

    day_counter += 1

if spend_days == 5:
    print(f"You can't save the money.\n{day_counter}")
elif money_available >= money_needed:
    print(f"You saved the money for {day_counter} days.")
