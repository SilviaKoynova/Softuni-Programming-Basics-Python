deposit = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())
monthly_interest = deposit * annual_interest_rate / 100 / 12
total_money = deposit + term_of_the_deposit * monthly_interest
print(total_money)
