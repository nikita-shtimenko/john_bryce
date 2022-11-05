def main():
    number = int(input("Enter number: "))

    fibonacci_sequence = generate_fibonacci_seq(number)
    next_number_index = len(fibonacci_sequence) - 1
    
    print(f"\n\
        Number: {number}.\n\
        Next number: {fibonacci_sequence[next_number_index]} [index: {next_number_index}]\n")

    return 1

def generate_fibonacci_seq(last_number: int) -> list[int]:
    sequence = [1, 1]

    temp_number = 0
    index = 2

    while True:
        temp_number = sequence[index - 2] + sequence[index - 1]
        sequence.append(temp_number)

        if temp_number > last_number:
            break

        index += 1

    return sequence

if __name__ == '__main__':
    main()