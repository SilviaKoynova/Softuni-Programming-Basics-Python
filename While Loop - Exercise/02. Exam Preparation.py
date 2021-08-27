total_bad_grades = int(input())
total_score = 0
number_of_problems = 0
last_problem = ""
too_many_bad_grades = False
command = input()
number_of_bad_grades = 0
while command != 'Enough':
    last_problem = command
    current_grade = int(input())
    if current_grade <= 4:
        number_of_bad_grades += 1
        if number_of_bad_grades == total_bad_grades:
            too_many_bad_grades = True
            break
    number_of_problems += 1
    total_score += current_grade



    command = input()
if too_many_bad_grades:
    print(f'You need a break, {number_of_bad_grades} poor grades.')
else:
    average_grade = total_score / number_of_problems
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')