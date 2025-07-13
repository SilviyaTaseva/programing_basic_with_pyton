import math

W = 2000
F = 1200
SF = 720

tournaments = int(input())
ranglist_point = int(input())
total_points = 0
precent_wins = 0
total_points = total_points + ranglist_point

for _ in range(tournaments):
    tournament_place = input()
    if tournament_place == 'W':
        total_points += W
        precent_wins += 1
    elif tournament_place == 'F':
        total_points += F
    elif tournament_place == 'SF':
        total_points += SF

if tournaments > 0:
    average_points = math.floor((total_points - ranglist_point) / tournaments)
    win_percentage = (precent_wins / tournaments) * 100
else:
    average_points = 0
    win_percentage = 0

print(f'Final points: {total_points:.0f}')
print(f'Average points: {average_points:.0f}')
print(f'{win_percentage:.2f}%')