def convert(fraction: str) -> int:
    a, b = fraction.split("/")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Invalid!  A and B must be integers")

    if b == 0:
        raise ZeroDivisionError("Invalid! B cannot be zero")

    if a > b:
        raise ValueError("Invalid! A cannot be greater than B")

    percentage = round(a / b * 100)
    if percentage < 0 or percentage > 100:
        raise ValueError("Invalid! Percentage must be between 0 and 100")

    return percentage


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


def main():
    fraction = input("Enter the fraction of the fuel tank filled (in X/Y format): ")
    try:
        percentage = convert(fraction)
        print("Gauge reading: " + gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print("Error: " + str(e))
        
main()