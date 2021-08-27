actor_name = input()
points_of_academy = float(input())
jury_num = int(input())
total_points = 0
isdone = False


for all_jury in range (jury_num):
    jury_name = input()
    points_from_jury = float(input())
    points = (len(jury_name) * points_from_jury) / 2
    total_points += points
    final = total_points + points_of_academy
    if final > 1250.5:
        isdone = True
        break
if isdone:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {final:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {abs(1250.5 - final):.1f} more!')





