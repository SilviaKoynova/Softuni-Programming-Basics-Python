name = input()
current_class = 1
final_score = 0
fails = 0
sum = 0
while current_class <= 12:
    grade = float(input())
    if grade < 4:
        fails +1
        if fails > 1:

            break
        continue
else:
    sum += grade
    print(f"{name} graduated. Average grade: {sum / 12}")
current_class += 1
if current_class == 13:
    print(f"{name} graduated. Average grade: {sum / 12:.2f}")
else:
    print(f"{name} has been excluded at {current_class} grade")


