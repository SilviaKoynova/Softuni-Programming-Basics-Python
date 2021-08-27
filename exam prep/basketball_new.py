matches_won = 0
matches_lost = 0
total_matches_count = 0
command = input()
while command != 'End of tournaments':
    tournament_name = command
    games_count = int(input())
    for game in range(1, games_count + 1):
        points = int(input())
        opponent_points = int(input())
        total_matches_count += 1
        diff = abs(points - opponent_points)
        if points > opponent_points:
            matches_won += 1
            print(f'Game {game} of tournament {tournament_name}: win with {diff} points.')
        else:
            matches_lost += 1
            print(f'Game {game} of tournament {tournament_name}: lost with {diff} points.')
    command = input()
print(f'{matches_won * 100 / total_matches_count:.2f}% matches win')
print(f'{matches_lost * 100 / total_matches_count:.2f}% matches lost')