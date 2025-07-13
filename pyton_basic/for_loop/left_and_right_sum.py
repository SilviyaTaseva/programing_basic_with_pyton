n = int(input())
num1 = 0
num2 = 0

for _ in range(n):
    current_number = int(input())
    num1 += current_number

for _ in range(n):
    current_number = int(input())
    num2 += current_number

if num1 == num2:
    print(f'Yes, sum = {num1}')
else:
    print(f'No, diff = {abs(num1 - num2)}')