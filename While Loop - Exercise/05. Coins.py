sum = float(input())
counter_coins = 0
sum = int(sum * 100)
counter_coins += sum // 200
sum = sum % 200
counter_coins += sum // 100
sum = sum % 100
counter_coins += sum // 50
sum = sum % 50
counter_coins += sum // 20
sum = sum % 20
counter_coins += sum // 10
sum = sum % 10
counter_coins += sum // 5
sum = sum % 5
counter_coins += sum // 2
sum = sum % 2
if sum == 1:
    counter_coins += 1
print(int(counter_coins))