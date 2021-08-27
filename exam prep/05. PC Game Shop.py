num_sold_games = int(input())
count_games = 0
sold_hearthstone = 0
sold_fornite = 0
sold_overwatch = 0
sold_others = 0
for all_games in range (num_sold_games):
    name_game = input()
    if name_game == 'Hearthstone':
        sold_hearthstone += 1
    elif name_game == 'Fornite':
        sold_fornite += 1
    elif name_game == 'Overwatch':
        sold_overwatch += 1
    else:
        sold_others += 1
hearthstone = sold_hearthstone / num_sold_games * 100
fortnite = sold_fornite / num_sold_games * 100
overwatch = sold_overwatch / num_sold_games * 100
others = sold_others / num_sold_games * 100
print(f'Hearthstone - {hearthstone:.2f}%')
print(f'Fornite - {fortnite:.2f}%')
print(f'Overwatch - {overwatch:.2f}%')
print(f'Others - {others:.2f}%')

