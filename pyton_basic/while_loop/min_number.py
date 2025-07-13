min_number = None

while True:
    comand = input()
    if comand == 'Stop':
        break

    current_number = int(comand)

    if min_number is None or current_number < min_number:
        min_number = current_number

print(min_number)