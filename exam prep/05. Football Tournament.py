W = 3
D = 1
L = 0
wins = 0
counter_w = 0
draws = 0
counter_draws = 0
loses = 0
counter_loses = 0
total_points = 0
team_name = input()
games_played = int(input())
if games_played <= 0:
    print(f"{team_name} hasn't played any games during this season.")
for each_game in range (1, games_played + 1):
    result = input()

    if result == 'W':
        wins += W
        counter_w += 1
    elif result == 'D':
       draws += D
       counter_draws += 1
    elif result == 'L':
       counter_loses += 1
    total_points = wins + draws
    percent_of_wins = counter_w / games_played * 100
if games_played > 0:
 print(f'{team_name} has won {total_points} points during this season.')
 print('Total stats:')
 print(f'## W: {counter_w}')
 print(f'## D: {counter_draws}')
 print(f'## L: {counter_loses}')

 print(f'Win rate: {percent_of_wins:.2f}%')
