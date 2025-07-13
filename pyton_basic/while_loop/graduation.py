schooler_name = input()
total_grades = 0
count_grades = 0
fail_count = 0
year = 1

while year <= 12:
    grades = float(input())

    while grades < 2 or grades > 6:
        print("Invalid grade. Please enter a grade between 2 and 6.")
        grades = float(input())

    if grades < 4:
        fail_count += 1
        if fail_count > 1:
            print(f"{schooler_name} has been excluded at {year} grade")
            break
    else:
        total_grades += grades
        count_grades += 1
        year += 1

if fail_count <= 1:
    average_grades = total_grades / count_grades
    print(f"{schooler_name} graduated. Average grade: {average_grades:.2f}")