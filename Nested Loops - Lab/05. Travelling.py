destination = input()
while destination != 'End':
    min_budget = float(input())
    money = float(input())
    saved = 0
    saved += money
    while saved < min_budget:
        money = float(input())
        saved += money
    else:
        print(f'Going to {destination}!')
    destination = input()