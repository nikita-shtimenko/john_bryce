import random

def main():
    july_2000_temp = generate_temp(30)
    july_2001_temp = generate_temp(30)
    july_2000_average_temp = sum(july_2000_temp) // 30

    index = 0

    for i in july_2001_temp:
        if i > july_2000_average_temp:
            print(f"Day: {index + 1}, temp: {i} | July 2000 AVG temp: {july_2000_average_temp}")

        index += 1
            
    return 1

def generate_temp(count: int) -> list[int]:
    if count <= 0:
        return None

    temp_list = []

    while count != 0:
        temp_list.append(random.randint(15, 40))
        count -= 1

    return temp_list

if __name__ == '__main__':
    main()