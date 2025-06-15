import math

movie_name = input()
episode_run = int(input())
total_break_time = int(input())

lunch_break = total_break_time / 8
relaxation_time = total_break_time / 4


lunch_and_relaxation = lunch_break + relaxation_time
break_time_left = total_break_time - lunch_and_relaxation


if break_time_left >= episode_run:
    break_time_left = math.ceil(break_time_left - episode_run)
    print(f"You have enough time to watch {movie_name} and left with {break_time_left} minutes free time.")
else:
    break_time_needed = math.ceil(episode_run - break_time_left)
    print(f"You don't have enough time to watch {movie_name}, you need {break_time_needed} more minutes.")