import re
import sys


def main():
    print(count(input("Input you text blow : \n")))


def count(s):
    patternword = r'\bum\b'
    matching = re.findall(patternword, s, flags=re.IGNORECASE)
    return len(matching)


if __name__ == "__main__":
    main()
