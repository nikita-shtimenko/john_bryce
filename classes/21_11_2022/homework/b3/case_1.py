def main():
    text = "green-red-yellow-black-white"
    result = sortWords(text)

    print(result)
    return 1

def sortWords(text: str) -> str:
    words = text.split('-')
    words.sort()

    return '-'.join(words)

if __name__ == '__main__':
    main()