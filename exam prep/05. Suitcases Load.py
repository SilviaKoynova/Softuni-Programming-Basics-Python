luggage_capacity = float(input())
command = input()
counter_suitcases = 0
while command != 'End':
    suitcase_volume = float(command)
    counter_suitcases += 1
    if counter_suitcases % 3 == 0:
        suitcase_volume *= 1.1
    luggage_capacity -= suitcase_volume
    if luggage_capacity < 0:
        print('No more space!')
        counter_suitcases -= 1
        break
    command = input()
if command == 'End':
    print('Congratulations! All suitcases are loaded!')
print(f'Statistic: {counter_suitcases} suitcases loaded.')