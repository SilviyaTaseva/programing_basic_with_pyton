
N1 = int(input())
N2 = int(input())
operator = input()

total = 0

if operator == '+':
    total = N1 + N2
    if total % 2 == 0:
      print(f'{N1} {operator} {N2} = {total} - even')
    else:
      print(f'{N1} {operator} {N2} = {total} - odd')
elif operator == '-':
    total = N1 - N2
    if total % 2 == 0:
     print(f'{N1} {operator} {N2} = {total} - even')
    else:
     print(f'{N1} {operator} {N2} = {total} - odd')
elif operator =='*':
    total = N1 * N2
    if total % 2 == 0:
     print(f'{N1} {operator} {N2} = {total} - even')
    else:
     print(f'{N1} {operator} {N2} = {total} - odd')

if operator == '/':
    if N2 == 0:
      print(f'Cannot divide {N1} by zero')
    else:
      total = N1 / N2
      print(f'{N1} / {N2} = {total:.2f}')
elif operator == '%':
    if N2 == 0:
      print(f'Cannot divide {N1} by zero')
    else:
      total = N1 % N2
      print(f'{N1} % {N2} = {total}')