days = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
sum_of_cakes = cakes * 45
sum_of_waffles = waffles * 5.80
sum_of_pancakes = pancakes * 3.20
sum_per_day = sum_of_cakes + sum_of_waffles + sum_of_pancakes
sum_per_day_confectioners = sum_per_day * confectioners
total_sum = sum_per_day_confectioners * days
final_price = total_sum - total_sum * 1/8
print(final_price)
