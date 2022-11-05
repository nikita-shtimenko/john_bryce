def main():
    index = int(input("Enter index: "))
    fibonacci_sequence = generate_fibonacci_seq(index)
    
    print(f"Index: {index}, number: {fibonacci_sequence[index]}")
    return 1

def generate_fibonacci_seq(last_index: int) -> list[int]:
    sequence = [1, 1]
    index = 2

    while index <= last_index:
        sequence.append((sequence[index - 2] + sequence[index - 1]))
        index += 1

    return sequence

if __name__ == '__main__':
    main()