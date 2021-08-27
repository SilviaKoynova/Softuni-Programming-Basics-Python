price_of_strawberries = float(input())
kg_of_bananas = float(input())
kg_of_oranges = float(input())
kg_of_raspberries = float(input())
kg_of_strawberries = float(input())
price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries - price_of_raspberries * 0.4
price_of_bananas = price_of_raspberries - price_of_raspberries * 0.8
sum_of_raspberries = kg_of_raspberries * price_of_raspberries
sum_of_oranges = kg_of_oranges * price_of_oranges
sum_of_bananas = kg_of_bananas * price_of_bananas
sum_of_strawberries = kg_of_strawberries * price_of_strawberries
total_sum = sum_of_raspberries + sum_of_oranges + sum_of_bananas + sum_of_strawberries
print(total_sum)
