num_pages = int(input())
pages_per_hour = int(input())
days = int(input())
total_time = num_pages / pages_per_hour
needed_hours = total_time / days
print(needed_hours)