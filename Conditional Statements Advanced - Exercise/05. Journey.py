budget = float(input())
season = input()
sum = 0
if budget <= 100:
    if season == "summer":
        sum = budget * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {sum:.2f}")
    else:
        sum = budget * 0.7
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {sum:.2f}")
elif budget <= 1000:
    if season == "summer":
        sum = budget * 0.4
        print(f"Somewhere in Balkans")
        print(f"Camp - {sum:.2f}")
    else:
        sum = budget * 0.8
        print(f"Somewhere in Balkans")
        print(f"Hotel - {sum:.2f}")
elif budget > 1000:
    sum = budget * 0.9
    print(f"Somewhere in Europe")
    print(f"Hotel - {sum:.2f}")
