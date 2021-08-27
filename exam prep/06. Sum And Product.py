from math import floor
n = int(input())
for a in range (1, 9 + 1):
    for b in range (9, a, - 1):
        for c in range (0, 9 + 1):
            for d in range (9, c, - 1):
                sum_n = a + b + c + d
                mult_n = a * b * c * d
                div1 = mult_n // sum_n
                div = int(div1)
                if sum == mult_n and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    break


                if div == 3  and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    break
                else:
                    print('Nothing found')









