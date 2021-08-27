
num_wins = 0
num_loses = 0
total_matches = 0
command = input()
while command != 'End of tournaments':
    name_of_tournament = command
    num_matches = int(input())
    total_matches += num_matches
    num_game = 0

    for every_match in range (num_matches):
        desi_team_points = int(input())
        rival_team_points = int(input())
        num_game += 1

        if desi_team_points > rival_team_points:
            num_wins += 1
            print(f'Game {num_game} of tournament {name_of_tournament}: win with {desi_team_points - rival_team_points} points.')
        else:
            num_loses += 1
            print(f'Game {num_game} of tournament {name_of_tournament}: lost with {rival_team_points - desi_team_points} points.')

    command = input()
if command == 'End of tournaments':
 percent_wins = num_wins / total_matches * 100
 percent_loses = num_loses / total_matches * 100
 print(f'{percent_wins:.2f}% matches win')
 print(f'{percent_loses:.2f}% matches lost')