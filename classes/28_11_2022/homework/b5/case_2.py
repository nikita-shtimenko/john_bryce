def main():
    colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 
        'purple', 'orange with white straps']

    print(getListUniqueElements(colors_2))
    return 1

def getListUniqueElements(input_list: list[str]) -> list[str]:
    values_data = dict()
    temp = None

    for value in input_list:
        temp = value.lower()

        if temp not in values_data:
            values_data[temp] = 1
        else:
            values_data[temp] += 1

    return [key for key, val in values_data.items() if val == 1]


if __name__ == '__main__':
    main()