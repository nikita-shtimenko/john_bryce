def main():
    text = "asa"
    result = isStringPalindrome(text)

    print(text, result)
    return 1

def isStringPalindrome(text: str) -> bool:
    return text == text[::-1]

if __name__ == '__main__':
    main()