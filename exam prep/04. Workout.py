from math import ceil
num_days = int(input())
km = float(input())
total_km = 0
allkm = km
for every_day in range (num_days):
    next_day = float(input())
    km = km + km * (next_day / 100)
    allkm += km
if allkm >= 1000:
    print(f"You've done a great job running {ceil(allkm - 1000)} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(1000 - allkm)} more kilometers')



