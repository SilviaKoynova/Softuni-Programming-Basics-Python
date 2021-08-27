command = input()
sum = 0
while command != "NoMoreMoney":
    number = float(command)
    if number < 0:
        print('Invalid operation!')
        break
    sum = sum + number
    print(f"Increase: {number:.2f}")
    command = input()
print(f'Total: {sum:.2f}')






