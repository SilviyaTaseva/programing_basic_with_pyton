number_of_cycles = int(input())
counter = 0

for _ in range(number_of_cycles):
    current_number = int(input())
    counter += current_number

print(counter)