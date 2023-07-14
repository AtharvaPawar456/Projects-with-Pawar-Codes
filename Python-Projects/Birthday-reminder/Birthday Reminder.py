# Birthday Reminder

import csv
import datetime

def load_birthdays():
    birthdays = []
    with open("birthdays.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Read the header row
        if header:
            for row in reader:
                name = row[0]
                date = datetime.datetime.strptime(row[1], "%Y-%m-%d").date()
                birthdays.append((name, date))
    return birthdays

def save_birthdays(birthdays):
    with open("birthdays.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date"])  # Write the header row
        for name, date in birthdays:
            writer.writerow([name, date.strftime("%Y-%m-%d")])

def show_birthdays(birthdays):
    print("\nBirthdays:")
    for name, date in birthdays:
        print(f"{name}: {date.strftime('%Y-%m-%d')}")

def add_birthday(name, date):
    birthdays = load_birthdays()
    birthdays.append((name, date))
    save_birthdays(birthdays)
    print("Birthday added successfully!")

# Test the birthday reminder
birthdays = load_birthdays()
show_birthdays(birthdays)

add_birthday("Pranit Pawar", datetime.date(2001, 6, 15))
add_birthday("Sahil Baikar", datetime.date(2003, 9, 20))

birthdays = load_birthdays()
show_birthdays(birthdays)


'''
=================================
Test Case:
=================================

Birthdays:
John Doe: 1990-06-15
Jane Smith: 1995-09-20
Birthday added successfully!
Birthday added successfully!

Birthdays:
John Doe: 1990-06-15
Jane Smith: 1995-09-20
Pranit Pawar: 2001-06-15
Sahil Baikar: 2003-09-20

'''