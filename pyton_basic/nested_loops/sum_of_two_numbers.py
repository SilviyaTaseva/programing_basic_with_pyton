num_start = int(input())
num_end = int(input())
magic_number = int(input())

combination_counter = 0
condition_break = False

for num1 in range(num_start, num_end + 1):
    for num2 in range(num_start, num_end + 1):
        combination_counter += 1
        if num1 + num2 == magic_number:
            print(f'Combination N:{combination_counter} ({num1} + {num2} = {magic_number})')

            condition_break = True
            break

    if condition_break:
        break
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')