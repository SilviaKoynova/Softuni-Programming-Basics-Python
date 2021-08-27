from math import floor
income = float(input())
average_mark = float(input())
minimum_wage = float(input())
social_scholarship = floor(0.35 * minimum_wage)
excellent_scholarship = floor(25 * average_mark)
if average_mark >= 5.50:
    if income < minimum_wage:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif average_mark > 4.5:
    if income < minimum_wage:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")














