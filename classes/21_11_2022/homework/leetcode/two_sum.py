def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = twoSum(numbers, 7)

    print(result)
    return 1

def twoSum(numbers: list[int], target: int) -> list[int]:
    result = []
    hashmap = {}

    for index, number in enumerate(numbers):
        temp = target - number

        if temp in hashmap.keys():
            result.extend([hashmap.get(temp), index])
            break

        hashmap[number] = index

    return result

if __name__ == '__main__':
    main()