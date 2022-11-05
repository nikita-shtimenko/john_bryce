def main():
    salary = float(input("Enter salary: "))
    salary_raise_percent = 0.10
    
    if salary * salary_raise_percent > 6000:
        salary_raise_percent = 0.05

    print(f"Salary with {salary_raise_percent * 100}% bonus: {salary + (salary * salary_raise_percent)}")
    return 1


if __name__ == '__main__':
    main()