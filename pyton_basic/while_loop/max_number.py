max_number = None

while True:
    comand = input()
    if comand == 'Stop':
        break

    current_number = int(comand)

    if max_number is None or current_number > max_number:
        max_number = current_number

print(max_number)