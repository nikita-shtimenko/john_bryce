strings_even_length_count = 0
count = 0

while count < 10:
    string = input("Enter a string: ")

    if len(string) % 2 == 0: # even
        strings_even_length_count += 1

    count += 1

print(f"Count of strings with even length: {strings_even_length_count}")