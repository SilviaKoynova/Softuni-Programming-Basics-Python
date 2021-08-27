name = input()
current_class = 1
final_score = 0
fails = 0
sum = 0
excluded = False
while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails == 2:
            excluded = True
            break
    else:

        sum += grade
        if current_class == 12:
            break
        current_class += 1
if excluded:
    print(f'{name} has been excluded at {current_class} grade')
else:
    print(f'{name} graduated. Average grade: {sum /12:.2f}')









