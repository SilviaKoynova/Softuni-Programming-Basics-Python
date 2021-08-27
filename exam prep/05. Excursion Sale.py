sea_travel = int(input())
mountain_travel = int(input())
profit = 0
counter_moutain = 0
counter_sea = 0
total_sea = 0
total_mountain = 0
total_m = 0
total_s = 0
command = input()
while command != 'Stop':
    ofer_name = command
    if ofer_name == 'sea':
        counter_sea += 1
        if counter_sea > sea_travel:
            total_sea += 0
        else:
            total_sea += 680
            total_s += total_sea

    if ofer_name == 'mountain':
        counter_moutain += 1
        if counter_moutain > mountain_travel:
            total_mountain += 0
        else:
            total_mountain += 499
            total_m += total_mountain
    total = total_mountain + total_sea
    if counter_moutain >= mountain_travel and counter_sea >= sea_travel:
        print('Good job! Everything is sold.')
        break


    command = input()
print(f'Profit: {total} leva.')

