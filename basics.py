import json

def check(choice):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
        print("No data found. A new file will be created.")
    except json.JSONDecodeError:
        data = {}
        print("Error reading JSON data. Starting with an empty dataset.")
    
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in data:
            print("Username already exists")
        else:
            data[username] = password
            with open("data.json", "w") as file:
                json.dump(data, file)
                print("User created successfully")
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in data:
            if data[username] == password:
                print("Login successful")
                print("Welcome, " + username)
                
            else:
                print("Incorrect password")
        else:
            print("Username does not exist")
    else:
        print("Invalid choice")

def main():
    print("1. Create user")
    print("2. Login")
    try:
        choice = int(input("Enter choice: "))
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
            return
        check(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")

main();
