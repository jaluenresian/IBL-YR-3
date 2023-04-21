def value(greeting: str) -> int:
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("hello"):
        return 0
    elif greeting_lower.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Enter your greeting: ")
    print("The value of your greeting is: " + str(value(greeting)))


if __name__ == "__main__":
    main()