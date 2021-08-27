#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
type_flower = input()
num_flower = int(input())
budget = int(input())
sum = 0
if type_flower == "Roses":
    sum = num_flower * 5
    if num_flower > 80:
        sum = sum * 0.9
elif type_flower == "Dahlias":
    sum = num_flower * 3.80
    if num_flower > 90:
        sum = sum * 0.85
elif type_flower == "Tulips":
    sum = num_flower * 2.80
    if num_flower > 80:
        sum = sum * 0.85
elif type_flower == "Narcissus":
    sum = num_flower * 3
    if num_flower < 120:
        sum = sum * 1.15
elif type_flower == "Gladiolus":
    sum = num_flower * 2.50
    if num_flower < 80:
        sum = sum * 1.20
if sum <= budget:
    print(f"Hey, you have a great garden with {num_flower} {type_flower} and {budget - sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum - budget:.2f} leva more.")