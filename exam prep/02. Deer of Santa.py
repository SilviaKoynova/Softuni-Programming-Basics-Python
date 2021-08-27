from math import ceil
from math import floor
days_missing_santa = int(input())
food = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())
first_deer = first_deer_food * days_missing_santa
second_deer = second_deer_food * days_missing_santa
third_deer = third_deer_food * days_missing_santa
total_needed_food = first_deer + second_deer + third_deer
difference = abs(total_needed_food - food)
if total_needed_food >= food:
    print(f'{ceil(difference)} more kilos of food are needed.')
else:
    print(f'{floor(difference)} kilos of food left.')
