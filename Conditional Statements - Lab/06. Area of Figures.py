from math import pi
from math import pow
type_figure = input()
if type_figure == "square":
    a = float(input())
    area_square = pow(a, 2)
    print(f"{area_square:.3f}")
elif type_figure == 'rectangle':
    a_r = float(input())
    b_r = float(input())
    area_rectangle = a_r * b_r
    print(f"{area_rectangle:.3f}")
elif type_figure == 'circle':
    r = float(input())
    area_circle = pi * pow(r, 2)
    print(f"{area_circle:.3f}")
elif type_figure == 'triangle':
    c = float(input())
    hc = float(input())
    area_triangle = (c * hc) / 2
    print(f"{area_triangle:.3f}")
