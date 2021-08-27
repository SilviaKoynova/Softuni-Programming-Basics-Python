fruit = input()
size = input()
q = int(input())
p = 0
if fruit == 'Watermelon':
    if size == 'small':
        p = q * 56 * 2
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
    elif size == 'big':
        p = q * 28.70 * 5
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
elif fruit == 'Mango':
    if size == 'small':
        p = q * 36.66 * 2
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
    elif size == 'big':
        p = q * 19.60 * 5
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
elif fruit == 'Pineapple':
    if size == 'small':
        p = q * 42.10 * 2
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
    elif size == 'big':
        p = q * 24.80 * 5
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
elif fruit == 'Raspberry':
    if size == 'small':
        p = q * 20 * 2
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
    elif size == 'big':
        p = q * 15.20 * 5
        if 400 <= p <= 1000:
            p *= 0.85
        elif p > 1000:
            p *= 0.5
print(f'{p:.2f} lv.')

