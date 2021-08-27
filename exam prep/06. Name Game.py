import sys
name = input()
winner_name = ""
total_points = 0
max_score = - sys.maxsize
while name != 'Stop':
    current_score = 0
    for letters in name:
        number = int(input())
        if int(number) == ord(letters):
            current_score += 10
        else:
            current_score += 2
        if current_score >= max_score:
            max_score = current_score
            winner_name = name
    name = input()
print(f'The winner is {winner_name} with {max_score} points!')

