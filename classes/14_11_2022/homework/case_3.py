EXIT_LOOP_CHAR = '#'

numbers_sum = 0
numbers_count = 0

while True:
    value = input(f"Enter a number ({EXIT_LOOP_CHAR} to stop): ")

    if value == EXIT_LOOP_CHAR:
        break

    if not value.isdigit():
        print("Error: invalid input. Please, enter a number.")
        continue

    numbers_sum += int(value)
    numbers_count += 1

print(f"Numbers sum: {numbers_sum}, average: {numbers_sum / numbers_count}")