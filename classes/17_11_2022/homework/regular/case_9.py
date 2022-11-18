number = int(input("Enter a number: "))

for i in range(1, number * 2):
    print('*' * i if i <= number else '*' * (number * 2 - i))
        