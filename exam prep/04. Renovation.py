from math import ceil
height = int(input())
width = int(input())
percentage_painted = float(input()) / 100
walls_for_painting = 0
walls_for_painting_final = 0
total = height * width * 4
walls_for_painting = ceil(total - (percentage_painted * total))
command = input()
while command != 'Tired!':
    liters_paint = int(command)


    walls_for_painting -= liters_paint
    if walls_for_painting <= 0:
        break

    command = input()

if walls_for_painting > 0:
    print(f'{walls_for_painting} quadratic m left.')
elif walls_for_painting == 0:
    print('All walls are painted! Great job, Pesho!')
else:
    print(f'All walls are painted and you have {abs(walls_for_painting)} l paint left!')