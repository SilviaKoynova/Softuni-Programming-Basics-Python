budget = float(input())
num_series = int(input())
total_money = 0
for each_series in range (num_series):
    series_name = input()
    cost = float(input())
    if series_name == 'Thrones':
        cost *= 0.5
        total_money += cost
    elif series_name == 'Lucifer':
        cost *= 0.6
        total_money += cost
    elif series_name == 'Protector':
        cost *= 0.7
        total_money += cost
    elif series_name == 'TotalDrama':
        cost *= 0.8
        total_money += cost
    elif series_name == 'Area':
        cost *= 0.9
        total_money += cost
    else:
        total_money += cost
if budget >= total_money:
    print(f'You bought all the series and left with {budget - total_money:.2f} lv.')
else:
    print(f'You need {abs(budget - total_money):.2f} lv. more to buy the series!')