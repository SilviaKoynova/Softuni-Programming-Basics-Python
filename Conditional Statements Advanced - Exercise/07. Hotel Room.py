month = input()
nights = int(input())
price_s = 0
price_a = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
price_s = studio * nights
price_a = apartment * nights
if 7 < nights <= 14 and (month == "May" or month == "October"):
    price_s = price_s * 0.95
elif  nights > 14 and (month == "May" or month == "October"):
    price_s = price_s * 0.7
elif nights > 14 and (month == "June" or month == "September"):
    price_s = price_s * 0.8
if nights > 14:
    price_a = price_a * 0.9
print(f"Apartment: {price_a:.2f} lv.")
print(f"Studio: {price_s:.2f} lv.")