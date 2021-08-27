number_of_days = int(input())
number_of_wins_in_all_days = 0
number_of_loses_in_all_days = 0
total_money = 0

for all_days in range (number_of_days):
    number_of_wins = 0
    number_of_loses = 0
    total_money_for_day = 0
    command = input()
    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            number_of_wins += 1
            total_money_for_day += 20
        else:
            number_of_loses += 1

        command = input()
    if number_of_wins > number_of_loses:
        total_money_for_day *= 1.1
        number_of_wins_in_all_days += 1
    else:
        number_of_loses_in_all_days += 1
    total_money += total_money_for_day
if number_of_wins_in_all_days > number_of_loses_in_all_days:
    total_money *= 1.2
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
