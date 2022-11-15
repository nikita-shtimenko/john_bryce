EXIT_LOOP_STRING = "$$$"

students_names = []
students_grades = []

while True:
    print() # new line

    name = input(f"Enter student name ({EXIT_LOOP_STRING} to stop): ")

    if name == EXIT_LOOP_STRING:
        break

    if not name.isalpha():
        print("Error: name: invalid input. All characters have to be letters")
        print("Start again...")
        continue

    grade = input(f"Enter student grade ({EXIT_LOOP_STRING} to stop): ")

    if grade == EXIT_LOOP_STRING:
        break

    if not grade.isdigit():
        print("Error: grade: invalid input. You have to enter a number.")
        print("Start again...")
        continue

    students_names.append(name.capitalize())
    students_grades.append(int(grade))

students_names_count = len(students_names)
index = 0

print("\nStudents names: \n")

while index < students_names_count:
    print(students_names[index])
    index += 1

print(f"\nStudents count: {students_names_count}")
print(f"Average grade: {sum(students_grades) / len(students_grades)}")