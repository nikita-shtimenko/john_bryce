import string

def main():
    text = "The quick brown fox jumps over the lazy dog"
    result = isPangramText(text)

    print(result)
    return 1

def isPangramText(text: str) -> bool:
    alphabet = tuple(string.ascii_lowercase)
    
    for char in alphabet:
        if text.count(char) == 0:
            return False

    return True

if __name__ == '__main__':
    main()