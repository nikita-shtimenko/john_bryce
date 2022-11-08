salary = int(input("Enter your salary: "))
tax = 0

if salary >= 220000:
    tax = (salary - 220000) * 0.5 + 68100
elif salary >= 120000:
    tax = (salary - 120000) * 0.4 + 29000
elif salary >= 46000:
    tax = (salary - 46000) * 0.3 + 6900
elif salary >= 23000:
    tax = (salary - 23000) * 0.2 + 2300
else:
    tax = salary * 0.1

print(f"Salary tax: {tax}")