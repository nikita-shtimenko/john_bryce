variables = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
result = []

for var in variables:
    if type(var) == int and var > 0:
        result.append(var)

print(variables)
print(result)