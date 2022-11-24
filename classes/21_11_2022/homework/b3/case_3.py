def main():
    text = "lEt mEE tEssTT yOU"
    result = getStringLetterCaseData(text)

    print(f"Lowercase: {result[0]}, Uppercase: {result[1]}")
    return 1

def getStringLetterCaseData(text: str) -> tuple[int, int]:
    count_lowercase = 0
    count_uppercase = 0

    for char in text:
        if char.isupper():
            count_uppercase += 1
        elif char.islower():
            count_lowercase += 1

    return (count_lowercase, count_uppercase)

if __name__ == '__main__':
    main()