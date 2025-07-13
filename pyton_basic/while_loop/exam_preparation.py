faild_exercise = int(input())
fail_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_faild = True

while fail_times < faild_exercise:
    problem_name = input()
    if problem_name == 'Enough':
        has_faild = False
        break
    grades = int(input())
    if grades <= 4:
        fail_times += 1
    grades_sum += grades
    solved_problems_count += 1
    last_problem = problem_name

if has_faild:
    print(f'You need a break, {faild_exercise} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_problems_count:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')