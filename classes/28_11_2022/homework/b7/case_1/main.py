from user import User

users = list()

def main():
    print(">>> Welcome to daily water tracker.")
    print("> Choose one from options below: ")
    return 1

def printUsersList() -> None:
    result = ">>> Active Users:\n"

    for i, user in enumerate(users):
        result += f"\n{i + 1}. {user.get_name()}"

    print(result)

def getUserObjectByName(name: str) -> User:
    result = None

    for user in users:
        if user.name_get() == name:
            return user

    return User("", -1)

if __name__ == '__main__':
    main()