EXIT_LOOP_STRING = "$"

strings_count = 0
chars_count = 0
numbers_count = 0
digits_count = 0

while True:
    value = input("Enter a value: ")

    if value == EXIT_LOOP_STRING:
        break

    if value.isdigit():
        numbers_count += 1
        digits_count += len(value)
        continue

    strings_count += 1
    chars_count += len(value)

print(f"Strings count: {strings_count}, chars count: {chars_count}")
print(f"Numbers count: {numbers_count}, digits count: {digits_count}")
    