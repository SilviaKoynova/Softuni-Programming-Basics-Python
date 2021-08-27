trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
income = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2
total_toys = puzzles + dolls + teddy_bears + minions + trucks
if total_toys >= 50:
   income = income - (income * 0.25)
total_value_rent = income - (income * 0.1)
if total_value_rent >= trip_price:
    moneyleft = total_value_rent - trip_price
    print(f"Yes! {moneyleft:.2f} lv left.")
else:
    money_needed = trip_price - total_value_rent
    print(f"Not enough money! {money_needed:.2f} lv needed.")



