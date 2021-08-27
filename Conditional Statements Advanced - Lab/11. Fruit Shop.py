
fruit = input()
day = input()
q = float(input())
price = 0
is_fruit = False
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = q * 2.50
    elif fruit == "apple":
        price = q * 1.20
    elif fruit == "orange":
        price = q * 0.85
    elif fruit == "grapefruit":
        price = q * 1.45
    elif fruit == "kiwi":
        price = q * 2.70
    elif fruit == "pineapple":
        price = q * 5.50
    elif fruit == "grapes":
        price = q * 3.85



if day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = q * 2.70
    elif fruit == "apple":
        price = q * 1.25
    elif fruit == "orange":
        price = q * 0.90
    elif fruit == "grapefruit":
        price = q * 1.60
    elif fruit == "kiwi":
        price = q * 3.00
    elif fruit == "pineapple":
        price = q * 5.60
    elif fruit == "grapes":
        price = q * 4.20
if price > 0:
    print(f"{price:.2f}")
else:
    print("error")







