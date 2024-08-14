"""
WAP that first gives 2 options: 
1. Sign up
2. Sign in

when 1 is pressed user needs to provide following information 
Username, 2. Password, 3. Mobile number
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 

-Jeena Nakarmi

"""

import json

def sign_up():
    username = input("Enter username: ")
    password = input("Enter password: ")
    mobile_number = input("Enter mobile number: ")

    user_data = {
        "username": username,
        "password": password,
        "mobile_number": mobile_number
    }

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(user_data)

    with open("users.json", "w") as file:
        json.dump(users, file)

    print("Sign-up successful!")

def sign_in():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome !! ")
            return

    print("Incorrect credentials! ")

def main():
    choice = input("Enter 1 to Sign up, or 2 to Sign in: ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
