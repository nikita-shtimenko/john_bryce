def main():
    value = "hello"
    result = reverseString(value)
    
    print(result)
    return 1

def reverseString(string: str) -> str:
    return string[::-1]

if __name__ == '__main__':
    main()