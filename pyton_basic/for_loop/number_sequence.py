n = int(input())
number = int(input())

max_n = number
min_n = number

for _ in range(1, n):
    current_num = int(input())
    if current_num > max_n:
        max_n = current_num
    if current_num < min_n:
        min_n = current_num

print(f'Max number: {max_n}')
print(f'Min number: {min_n}')