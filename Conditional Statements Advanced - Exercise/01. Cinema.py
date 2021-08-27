screening_type = input()
rows = int(input())
columns = int(input())
total = 0
if screening_type == "Premiere":
    total = rows * columns * 12
elif screening_type == "Normal":
    total = rows * columns * 7.50
elif screening_type == "Discount":
    total = rows * columns * 5
print(f"{total:.2f} leva")
