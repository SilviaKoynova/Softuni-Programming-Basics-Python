num_dancers = int(input())
num_points = float(input())
season = input()
place = input()
if place == 'Bulgaria':
    if season == 'summer':
        sum_per_one = num_dancers * num_points
        sum_per_one *= 0.95
    if season == 'winter':
        sum_per_one = num_dancers * num_points
        sum_per_one *= 0.92

if place == 'Abroad':
    if season == 'summer':
       sum_per_one = num_dancers * num_points
       sum_per_one *= 1.5
       sum_per_one *= 0.9

    if season == 'winter':
       sum_per_one = num_dancers * num_points
       sum_per_one *= 1.5
       sum_per_one *= 0.85
charity_money = sum_per_one * 0.75
left_money = sum_per_one - charity_money
dancer = left_money / num_dancers
print(f'Charity - {charity_money:.2f}')
print(f'Money per dancer - {dancer:.2f}')

