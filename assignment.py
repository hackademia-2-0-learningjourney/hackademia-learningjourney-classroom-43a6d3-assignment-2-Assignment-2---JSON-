import json
import os

print('1.Sign up \n 2.Sign in')
choice = int(input("Enter your choice: "))
if choice == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    mob = input("Enter mobile number: ")

    invalues = {}

    if(os.path.isfile('./signupinfo.json')):
        with open('signupinfo.json', 'r') as f:
            invalues = json.load(f)

    invalues[username] = {
        'password' : password,
        'mobilenumber' : mob,
    }

    with open('signupinfo.json', 'w') as f:
        json.dump(invalues, f)
else:
    flag= 0
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('signupinfo.json', 'r') as f:
        values = json.load(f)
        for x in values:
            if(username == x and password == values[x]['password']):
                print("welcome to the program")
                print("your info")
                print("username: " + x)
                print("password: " + values[x]['password'])
                print("mobile number: " + values[x]['mobilenumber'])
                flag = 0
                break
            else:
                flag = 1
    if flag == 1:
        print("Login failed")
