jury = int(input())
command = input()
final_grade = 0
counter_exams = 0
while command != 'Finish':
    presentation_name = command
    average_grade = 0
    for grades in range (jury):
        current_grade = float(input())
        average_grade += current_grade
        counter_exams += 1
        final_grade += current_grade
    average_grade /= jury
    print(f'{presentation_name} - {average_grade:.2f}.')

    command = input()
final_grade /= counter_exams
print(f"Student's final assessment is {final_grade:.2f}.")