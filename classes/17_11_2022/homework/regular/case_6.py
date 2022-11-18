number = int(input("Enter a number: "))
series = int(input("Enter a series count: "))

total_sum = 0
output_str = ""

for i in range(1, series + 1):
    output_str += f"{str(number) * i}{' + ' if i != series else ''}"
    total_sum += int(f"{str(number) * i}")

print(f"{output_str} = {total_sum}")