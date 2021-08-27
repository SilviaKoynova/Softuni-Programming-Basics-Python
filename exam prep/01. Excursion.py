total_people = int(input())
num_sleepovers = int(input())
transport_cards_num = int(input())
museums_tickets_num = int(input())
nights_price = num_sleepovers * 20
transport_price = transport_cards_num * 1.60
museum_price = museums_tickets_num * 6
total_sum = nights_price + transport_price + museum_price
total_sum_for_everyone = total_sum * total_people
total_sum_for_everyone *= 1.25
print(f'{total_sum_for_everyone:.2f}')