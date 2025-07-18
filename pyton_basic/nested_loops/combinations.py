n = int(input())
combination_count = 0

for number_1 in range(0,n + 1):
    for number_2 in range(0, n + 1):
        for number_3 in range(0, n + 1):
            if number_1 + number_2 + number_3 == n:
              combination_count +=1
print(f'{combination_count}')