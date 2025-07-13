gabi_goal = 10_000
steps_count = 0


while steps_count < gabi_goal:
    command = input()

    if command == 'Going home':
        going_home = int(input())
        steps_count += going_home
        break

    steps_count += int(command)

if steps_count >= gabi_goal:
    print(f'Goal reached! Good job!\n{steps_count - gabi_goal} steps over the goal!')
else:
    print(f'{gabi_goal - steps_count} more steps to reach goal.')





