product = input()
city = input()
q = float(input())
if city == "Sofia":
    if product == "coffee":
        print(q * 0.50)
    elif product == "water":
        print(q * 0.80)
    elif product == "beer":
        print(q * 1.20)
    elif product == "sweets":
        print(q * 1.45)
    elif product == "peanuts":
        print(q * 1.60)
if city == "Plovdiv":
    if product == "coffee":
        print(q * 0.40)
    elif product == "water":
        print(q * 0.70)
    elif product == "beer":
        print(q * 1.15)
    elif product == "sweets":
        print(q * 1.30)
    elif product == "peanuts":
        print(q * 1.50)
if city == "Varna":
    if product == "coffee":
        print(q * 0.45)
    elif product == "water":
        print(q * 0.70)
    elif product == "beer":
        print(q * 1.10)
    elif product == "sweets":
        print(q * 1.35)
    elif product == "peanuts":
        print(q * 1.55)