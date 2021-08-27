rent_place = int(input())
price_of_cake = rent_place * 0.2
price_of_drinks = price_of_cake - price_of_cake * 0.45
animator = rent_place * 1/3
total_sum = rent_place + price_of_cake + price_of_drinks + animator
print(total_sum)
