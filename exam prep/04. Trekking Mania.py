count_groups = int(input())
musala = 0

monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0
for each_group in range (count_groups):
    people = int(input())
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilimanjaro += people
    elif 26 <= people <= 40:
        k2 += people
    elif people >= 41:
        everest += people
total_people = musala + monblan + kilimanjaro + k2 + everest
musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimanjaro_percent = kilimanjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100
print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

