import re
import sys


def main():
    print(count(input("Input you text blow : \n")))


def count(s):
    patt = r'\bum\b'
    match = re.findall(patt, s, flags=re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()