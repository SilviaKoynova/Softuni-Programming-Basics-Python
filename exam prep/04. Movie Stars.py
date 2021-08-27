budget = float(input())
command = input()
while command != 'ACTION':

    if len(command) > 15:
        budget -= budget * 0.20
    else:
        money = float(input())
        budget -= money
    if budget < 0:
        break
    command = input()
if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')