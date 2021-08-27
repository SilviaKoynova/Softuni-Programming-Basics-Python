goal_income = float(input())
command = input()
total_income = 0
while command != 'Party!':
    cocktail_name = command
    num_cocktail_in_order = int(input())
    price_per_order = len(cocktail_name) * num_cocktail_in_order
    if price_per_order % 2 != 0:
        price_per_order *= 0.75
    total_income += price_per_order
    if total_income >= goal_income:
        print('Target acquired.')
        break
    command = input()
difference = abs(total_income - goal_income)
if command == 'Party!':
    print(f'We need {difference:.2f} leva more.')
print(f'Club income - {total_income:.2f} leva.')
