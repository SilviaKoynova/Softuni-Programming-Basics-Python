number = float(input())
metric = input()
metric_to_convert = input()
convert_to_metres = 0
if metric == "mm":
    convert_to_metres = number / 1000
elif metric == "cm":
    convert_to_metres = number / 100
else:
    convert_to_metres = number
result = 0
if metric_to_convert == "mm":
    result =  convert_to_metres * 1000
elif metric_to_convert == "cm":
    result = convert_to_metres * 100
else:
    result = convert_to_metres
print(f"{result:.3f}")
