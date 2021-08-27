days = int(input())
type_room = input()
grade = input()
final_price = 0
single = 18
apartment = 25
president = 35
nights = days - 1
if type_room == "room for one person":
    final_price = nights * single
elif type_room == "apartment":
    final_price = nights * apartment
    if days < 10:
        final_price = final_price * 0.7
    elif 10 <= days <= 15:
        final_price = final_price * 0.65
    else:
        final_price = final_price * 0.5
elif type_room == "president apartment":
    final_price = nights * president
    if days < 10:
        final_price = final_price * 0.9
    elif 10 <= days <= 15:
        final_price = final_price * 0.85
    else:
        final_price = final_price * 0.8
if grade == "positive":
    final_price = final_price * 1.25
    print(f"{final_price:.2f}")
else:
    final_price = final_price * 0.9
    print(f"{final_price:.2f}")