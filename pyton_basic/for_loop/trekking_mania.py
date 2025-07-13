tracking_group = int(input())

for_musala = 0
for_monblanc = 0
for_kilimanjaro = 0
for_k2 = 0
for_everest = 0

for _ in range(tracking_group):
    people_in_group = int(input())
    if people_in_group <= 5:
        for_musala += people_in_group
    elif 6 <= people_in_group <= 12:
        for_monblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        for_kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        for_k2 += people_in_group
    else:
        for_everest += people_in_group

total_people = for_musala + for_monblanc + for_kilimanjaro + for_k2 + for_everest

precent_musala = for_musala / total_people * 100
precent_monblanc = for_monblanc / total_people * 100
precent_kilimanjaro = for_kilimanjaro / total_people * 100
precent_k2 = for_k2 / total_people * 100
precent_everest = for_everest / total_people * 100

print(f'{precent_musala:.2f}%')
print(f'{precent_monblanc:.2f}%')
print(f'{precent_kilimanjaro:.2f}%')
print(f'{precent_k2:.2f}%')
print(f'{precent_everest:.2f}%')




