from math import  floor
record = float(input())
distance_in_metres = float(input())
time_in_seconds = float(input())
distance_needed = distance_in_metres * time_in_seconds
slowing = floor(distance_in_metres / 15)
slowing_add = slowing * 12.5
total_time = slowing_add + distance_needed
if record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")