import sys

number_elements = int(input())
max_elements = - sys.maxsize
sum_elements = 0

for _ in range(number_elements):
    num = int(input())

    if num > max_elements:
        max_elements = num

    sum_elements += num

half_sum = sum_elements - max_elements

if half_sum == max_elements:
    print('Yes')
    print(f'Sum = {half_sum}')
else:
    print('No')
    print(f'Diff = {abs(max_elements - half_sum)}')