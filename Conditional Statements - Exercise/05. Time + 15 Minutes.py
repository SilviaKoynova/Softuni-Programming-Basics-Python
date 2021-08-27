hours = int(input())
minutes = int(input())
hours_in_minutes = hours * 60 + minutes
minutes_plus_fifteen = hours_in_minutes + 15
final_hours = minutes_plus_fifteen // 60
final_minutes = minutes_plus_fifteen % 60
if final_hours == 24:
    final_hours = 0
if final_minutes < 10:
    print(f"{final_hours}:0{final_minutes}")
else:
    print(f"{final_hours}:{final_minutes}")