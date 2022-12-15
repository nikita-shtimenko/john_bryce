def main():
    flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
    color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']

    result = generateDictFromLists(flowers, color)
    print(result)
    return 1

def generateDictFromLists(list_first: list, list_second: list) -> dict:
    result_dict = {}

    for first_elem, second_elem in zip(list_first, list_second):
        if not first_elem in result_dict:
            result_dict[first_elem] = [second_elem]
        else:
            result_dict[first_elem].append(second_elem)

    return result_dict

if __name__ == "__main__":
    main()