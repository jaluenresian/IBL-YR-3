import sys
from datetime import date, datetime

def main():
    dob_str = input("Please enter your date of birth (YYYY-MM-DD): ")
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        sys.exit(1)
    
    today = date.today()
    age_in_minutes = int((today - dob).total_seconds() // 60)
    print("You are", convert_to_english_words(age_in_minutes), "old in minutes.")

def convert_to_english_words(minutes):
    words = []

    years = minutes // 525600
    if years > 0:
        words.append(convert_to_english_words(years) + " year" + ("s" if years > 1 else ""))

    minutes %= 525600
    months = minutes // 43800
    if months > 0:
        words.append(convert_to_english_words(months) + " month" + ("s" if months > 1 else ""))

    minutes %= 43800
    weeks = minutes // 10080
    if weeks > 0:
        words.append(convert_to_english_words(weeks) + " week" + ("s" if weeks > 1 else ""))

    minutes %= 10080
    days = minutes // 1440
    if days > 0:
        words.append(convert_to_english_words(days) + " day" + ("s" if days > 1 else ""))

    minutes %= 1440
    hours = minutes // 60
    if hours > 0:
        words.append(convert_to_english_words(hours) + " hour" + ("s" if hours > 1 else ""))

    minutes %= 60
    if minutes > 0:
        words.append(str(minutes) + " minute" + ("s" if minutes > 1 else ""))

    if not words:
        return "0 minutes"

    return " ".join(words)

if __name__ == "__main__":
    main()