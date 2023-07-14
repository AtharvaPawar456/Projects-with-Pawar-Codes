# Password Manager

import json
import getpass

PASSWORD_FILE = 'passwords.json'

def load_passwords():
    try:
        with open(PASSWORD_FILE, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    
    return passwords

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def add_password(passwords, website, username, password):
    passwords[website] = {
        'username': username,
        'password': password
    }
    save_passwords(passwords)
    print("Password added successfully!")

def get_password(passwords, website):
    if website in passwords:
        return passwords[website]
    else:
        return None

def delete_password(passwords, website):
    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Website not found in the password manager.")

def main_menu():
    print("Password Manager")
    print("-----------------")
    print("1. Add a password")
    print("2. Get a password")
    print("3. Delete a password")
    print("4. Exit")

def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_credentials():
    website = input("Website: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return website, username, password

# Load passwords from file
passwords = load_passwords()

# Main program loop
while True:
    main_menu()
    choice = get_menu_choice()

    if choice == '1':
        website, username, password = get_credentials()
        add_password(passwords, website, username, password)
    elif choice == '2':
        website = input("Website: ")
        stored_password = get_password(passwords, website)
        if stored_password:
            print("Username:", stored_password['username'])
            print("Password:", stored_password['password'])
        else:
            print("Website not found in the password manager.")
    elif choice == '3':
        website = input("Website: ")
        delete_password(passwords, website)
    elif choice == '4':
        break

print("Goodbye!")






'''
=================================
Test Case:
=================================

Password Manager
-----------------
1. Add a password
2. Get a password
3. Delete a password
4. Exit
Enter your choice (1-4): 1
Website: www.instagram.com
Username: testname
Password:
Password added successfully!
Password Manager
-----------------
1. Add a password
2. Get a password
3. Delete a password
4. Exit
Enter your choice (1-4): 2
Website: www.instagram.com
Username: testname
Password: testpassword
Password Manager
-----------------
1. Add a password
2. Get a password
3. Delete a password
4. Exit
Enter your choice (1-4): 3
Website: www.instagram.com
Password deleted successfully!
Password Manager
-----------------
1. Add a password
2. Get a password
3. Delete a password
4. Exit
Enter your choice (1-4): 4
Goodbye!

'''