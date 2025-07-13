number_elements = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for _ in range(number_elements):
    current_num = int(input())

    if current_num < 200:
        count_p1 += 1
    elif 200 <= current_num <= 399:
        count_p2 += 1
    elif 400 <= current_num <= 599:
        count_p3 += 1
    elif 600 <= current_num <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

precent_p1 = count_p1 / number_elements * 100
precent_p2 = count_p2 / number_elements * 100
precent_p3 = count_p3 / number_elements * 100
precent_p4 = count_p4 / number_elements * 100
precent_p5 = count_p5 / number_elements * 100

print(f'{precent_p1:.2f}%')
print(f'{precent_p2:.2f}%')
print(f'{precent_p3:.2f}%')
print(f'{precent_p4:.2f}%')
print(f'{precent_p5:.2f}%')