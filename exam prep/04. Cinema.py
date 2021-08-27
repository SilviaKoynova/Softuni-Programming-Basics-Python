capacity = int(input())
counter = 0
total_sum = 0
command = input()

while command != 'Movie time!':
    count_people = int(command)
    counter += count_people
    if counter > capacity:
        print('The cinema is full.')
        break
    if count_people % 3 == 0:
        cost_per_ticket = (5 * count_people) - 5
        total_sum += cost_per_ticket
    else:
        cost_per_ticket = 5 * count_people
        total_sum += cost_per_ticket

    command = input()

if command == 'Movie time!' or counter == capacity:
    free_spaces = capacity - counter
    print(f'There are {free_spaces} seats left in the cinema.')
print(f'Cinema income - {total_sum} lv.')