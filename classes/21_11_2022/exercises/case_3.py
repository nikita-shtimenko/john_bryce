def main():
    result = getMaxValue(2.0, 4.0, 6.0)
    print(result)
    return 1

def getMaxValue(value_first: float, value_second: float, value_third: float) -> float:
    values = [value_first, value_second, value_third]
    return float(max(values))

if __name__ == '__main__':
    main()