def main():
    result = getMaxValue(2.0, 4.0, 6.0)
    print(result)
    return 1

def getMaxValue(value_first: float, value_second: float, value_third: float) -> float:
    result = float('inf')

    if value_first > value_second and value_first > value_third:
        result = value_first
    
    elif value_second > value_first and value_second > value_third:
        result = value_second

    elif value_third > value_first and value_third > value_second:
        result = value_third
        
    return result

if __name__ == '__main__':
    main()