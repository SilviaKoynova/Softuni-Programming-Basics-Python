from math import floor
days = int(input())
bought_food = float(input())
total_food_dog = 0
total_eaten_cat = 0
biscuits = 0
total_food = 0
final = 0
dog = 0
cat = 0
for all_days in range (1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    total_food_dog += dog_eaten
    total_eaten_cat += cat_eaten
    if all_days % 3 == 0:
        current_biscuits = (dog_eaten + cat_eaten) * 0.1
        biscuits += current_biscuits
total_food = total_food_dog + total_eaten_cat
final = total_food / bought_food * 100
dog = total_food_dog / total_food * 100
cat = total_eaten_cat / total_food * 100
print(f'Total eaten biscuits: {floor(biscuits)}gr.')
print(f'{final:.2f}% of the food has been eaten.')
print(f'{dog:.2f}% eaten from the dog.')
print(f'{cat:.2f}% eaten from the cat.')
