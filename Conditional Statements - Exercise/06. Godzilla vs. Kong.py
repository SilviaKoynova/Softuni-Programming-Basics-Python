budget = float(input())
statist = int(input())
price_clothes = float(input())
decor = budget * 0.1
discount = 0
final_price_clothes = price_clothes * statist
if statist > 150:
    discount = final_price_clothes * 0.1
    final_price_clothes = final_price_clothes - discount
total_sum = decor + final_price_clothes
total = budget - total_sum
if total_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - budget:.2f} leva more.")



