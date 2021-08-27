lenght = int(input())
width = int(input())
height = int(input())
percentage_of_volume = float(input())
volume = lenght * width * height
liters_to_dm = volume * 0.001
percentage_calc = percentage_of_volume / 100
liters_needed = liters_to_dm - liters_to_dm * percentage_calc
print(liters_needed)
