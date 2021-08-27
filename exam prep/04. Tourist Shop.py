budget = float(input())
counter_products = 0
total_price = 0
command = input()
while command != 'Stop':
    product_name = command
    price_for_product = float(input())
    counter_products += 1
    if counter_products % 3 == 0:
        price_for_product /= 2
        total_price += price_for_product
    else:
       total_price += price_for_product
    if total_price > budget:
        print("You don't have enough money!")
        print(f'You need {abs(total_price - budget):.2f} leva!')
        break
    command = input()
if command == 'Stop':
    print(f'You bought {counter_products} products for {total_price:.2f} leva.')
