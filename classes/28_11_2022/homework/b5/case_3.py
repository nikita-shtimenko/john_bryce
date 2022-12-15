def main():
    colors_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
    colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']

    print(getDuplicatedColors(colors_1, colors_2))
    return 1

def getDuplicatedColors(colors_1: list[str], colors_2: list[str]) -> list[str]:
    result = list()

    second_list_items_lower = tuple(i.lower() for i in colors_2)
    temp = None

    for i in colors_1:
        temp = i.lower()

        if temp in result:
            continue

        if temp not in second_list_items_lower:
            continue
            
        result.append(temp)

    return result

if __name__ == '__main__':
    main()