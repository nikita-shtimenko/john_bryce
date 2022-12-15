def main():
    colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 
        'pure purple', 'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 
        'Egyptian blue', 'Neon blue']
    
    colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 
        'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']

    print(getUniqueDifferentColors(colors_1, colors_2))
    return 1

def getUniqueDifferentColors(colors_1: list[str], colors_2: list[str]) -> set:
    return set(i for i in colors_1).difference(set(i for i in colors_2))

if __name__ == '__main__':
    main()