def main():
    test = "print(5 + 1)"
    result = executeCode(test)
    print(result)
    return 1

def executeCode(text: str) -> bool:
    if not len(text):
        print("")
        return False
    
    exec(text)
    return True

if __name__ == '__main__':
    main()