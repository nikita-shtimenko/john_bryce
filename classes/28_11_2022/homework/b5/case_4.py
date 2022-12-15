def main():
    basic_colors = ['red', 'blue', 'Purple','white']

    colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 
        'pure purple', 'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 
        'Egyptian blue', 'Neon blue']
    
    colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue', 
        'Pale purple', 'Orchid purple', 'BLUE pure']

    print(getColorsDerivedFromBasic(basic_colors, [colors_1, colors_2]))
    return 1

def getColorsDerivedFromBasic(basic_colors: list[str], colors: list[list[str]]) -> list[str]:
    result = list()
    temp = None

    for colors_list in colors:
        for color in colors_list:
            temp = color.lower()

            if temp in result:
                continue

            if not isColorDerivedFromBasic(basic_colors, temp):
                continue

            result.append(temp)

    return result

def isColorDerivedFromBasic(basic_colors: list[str], color: str) -> bool:
    for basic_color in basic_colors:
        if basic_color.lower() in color:
            return True
        
    return False

if __name__ == '__main__':
    main()