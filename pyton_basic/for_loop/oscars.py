min_points = 1250.5
star_name = input()
academy_points = float(input())
judges = int(input())

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    academy_points += (len(judge_name) * judge_points / 2)

    if academy_points > min_points:
        print(f'Congratulations, {star_name} got a nominee for leading role with {academy_points:.1f}!')
        break
else:
    needed_points = min_points - academy_points
    print(f'Sorry, {star_name} you need {needed_points:.1f} more!')