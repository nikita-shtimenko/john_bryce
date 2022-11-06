def main():
    number = int
    temp_fibonacci_sequence = []

    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Error: you have to enter a number.")
            continue

        if number == 0:
            print("Stop.")
            break

        temp_fibonacci_sequence = generate_fibonacci_seq(number)
        print(f"\n\
                {temp_fibonacci_sequence}")

        if number in temp_fibonacci_sequence:
            print(f"""
                Yes | Number {number} appears in fibonacci sequence.
                Position: {temp_fibonacci_sequence.index(number)}
                """)
        else:
            print(f"\
                No | Number {number} does not appear in fibonacci sequence.")
        
    return 1

def generate_fibonacci_seq(number: int) -> list[int]:
    if number <= 3:
        return None

    sequence = [1, 1]

    temp_number = 0
    index = 2

    while True:
        temp_number = sequence[index - 2] + sequence[index - 1]
        sequence.append(temp_number)

        if temp_number > number:
            break

        index += 1

    return sequence

if __name__ == '__main__':
    main()