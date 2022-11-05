def main():
    grade = int(input("Enter your grade: "))

    if grade not in range(0, 100 + 1):
        print("Error: grade has to be in range from 0 to 100.")
        return main()

    grade_value_range = (
        (0, 54),
        (55, 64),
        (65, 74),
        (75, 84),
        (85, 94),
        (94, 100)
    )

    grade_value_status = (
        "Not enough",
        "Enough",
        "Almost good",
        "Good",
        "Very good",
        "Excellent"
    )

    for value in grade_value_range:
        if grade in range(value[0], value[1] + 1):
            print(f"Grade: {grade}. Your grade is {grade_value_status[grade_value_range.index(value)]}")
            break

        continue
        
    return 1


if __name__ == '__main__':
    main()