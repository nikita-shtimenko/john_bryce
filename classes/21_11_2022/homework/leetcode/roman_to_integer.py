def main():
    roman = "MCMXCIV"
    result = romanToInt(roman)

    print(result)
    return 1

def romanToInt(text: str) -> int:
        roman_data = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        result = 0
        current_value = None

        for i in range(len(text) - 1):
            current_value = roman_data[text[i]]

            if current_value < roman_data[text[i + 1]]:
                result -= current_value
            else:
                result += current_value

        return result + roman_data[text[-1]]

if __name__ == '__main__':
     main()