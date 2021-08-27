sum = float(input())
gender = input()
age = int(input())
sport = input()
final = 0
if sport == 'Gym':
    if gender == 'm':
        if age > 19:
            final = 42
        else:
            final = 42
            final *= 0.8
    else:
        if age > 19:
            final = 35
        else:
            final = 35
            final *= 0.8
elif sport == 'Boxing':
    if gender == 'm':
        if age > 19:
            final = 41
        else:
            final = 41
            final *= 0.8
    else:
        if age > 19:
            final = 37
        else:
            final = 37
            final *= 0.8
elif sport == 'Yoga':
    if gender == 'm':
        if age > 19:
            final = 45
        else:
            final = 45
            final *= 0.8
    else:
        if age > 19:
            final = 42
        else:
            final = 42
            final *= 0.8
elif sport == 'Zumba':
    if gender == 'm':
        if age > 19:
            final = 34
        else:
            final = 34
            final *= 0.8
    else:
        if age > 19:
            final = 31
        else:
            final = 31
            final *= 0.8
elif sport == 'Dances':
    if gender == 'm':
        if age > 19:
            final = 51
        else:
            final = 51
            final *= 0.8
    else:
        if age > 19:
            final = 53
        else:
            final = 53
            final *= 0.8
elif sport == 'Pilates':
    if gender == 'm':
        if age > 19:
            final = 39
        else:
            final = 39
            final *= 0.8
    else:
        if age > 19:
            final = 37
        else:
            final = 37
            final *= 0.8
difference = abs(final - sum)
if final <= sum:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")