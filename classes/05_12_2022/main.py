def main():
    test = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
    print(getListOfDictFromDict(test))

def getListOfDictFromDict(input_dict: dict) -> list[dict]:
    result = list()
    outer_index = 0

    for key, values_list in input_dict.items():
        
        for index, value in enumerate(values_list):
            if outer_index == 0:
                result.append({key: value})
            else:
                result[index][key] = value

        outer_index += 1

    return result

if __name__ == '__main__':
    main()