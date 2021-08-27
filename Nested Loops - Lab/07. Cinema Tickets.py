total_sold_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
command = input()
while command != 'Finish':
    movie_name = command
    tickets_for_sale = int(input())
    sold_tickets = 0

    while sold_tickets < tickets_for_sale:
        type_of_the_ticket = input()
        if type_of_the_ticket == 'End':
            break
        elif type_of_the_ticket == 'student':
            total_student_tickets += 1
        elif type_of_the_ticket == "standard":
            total_standard_tickets += 1
        elif type_of_the_ticket == "kid":
            total_kids_tickets += 1
        sold_tickets += 1
        total_sold_tickets += 1

    percent_of_full_hall = sold_tickets / tickets_for_sale * 100
    print(f'{movie_name} - {percent_of_full_hall:.2f}% full.')
    command = input()
print(f'Total tickets: {total_sold_tickets}')
percent_of_student_tickets = total_student_tickets / total_sold_tickets * 100
print(f'{percent_of_student_tickets:.2f}% student tickets.')
percent_of_standard_tickets = total_standard_tickets / total_sold_tickets * 100
print(f'{percent_of_standard_tickets:.2f}% standard tickets.')
percent_of_kids_tickets = total_kids_tickets / total_sold_tickets * 100
print(f'{percent_of_kids_tickets:.2f}% kids tickets.')
