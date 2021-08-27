number = int(input())
if number <= 100:
    bonus = 5
elif 101 <= number <= 1000:
    bonus = 0.2 * number
else:
    bonus = number * 0.1
if number % 2 == 0:
    bonus = bonus + 1
elif number % 5 == 0:
    bonus = bonus + 2
print(bonus)
print(bonus + number)



