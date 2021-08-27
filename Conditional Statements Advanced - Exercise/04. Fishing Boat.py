budget = int(input())
season = input()
fishers = int(input())
sum = 0
if season == "Spring":
    sum = 3000
elif season == "Summer" or season == "Autumn":
    sum = 4200
elif season == "Winter":
    sum = 2600
if fishers <= 6:
    sum = sum * 0.9
elif 7 <= fishers <= 11:
    sum = sum * 0.85
elif fishers >= 12:
    sum = sum * 0.75
if fishers % 2 == 0 and season != "Autumn":
    sum = sum * 0.95
difference = abs(budget - sum)
if budget >= sum:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

