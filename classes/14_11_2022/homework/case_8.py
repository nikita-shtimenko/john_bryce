number = int(input("Enter a number: "))
digits_count = 0

while number != 0:
    number //= 10
    digits_count += 1

print(f"Digits count: {digits_count}")