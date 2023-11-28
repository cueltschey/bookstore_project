from Bookstore.User import User 
from Bookstore.Inventory import Inventory
from Bookstore.Cart import Cart


user = User("Bookstore/User.db", "User")
inventory = Inventory("Bookstore/Inventory.db", "Inventory")
print("Login Page:", "\n")

print("1. Login to existing account.")
print("2. Register a new account.")
print("3. Logout.")
option = input("Input option here: ")

while(option not in '123' or user.loggedIn == False):
    if(option == '1'):
        user.login()
    elif(option == '2'):
        user.createAccount()
    elif(option == '3'):
        user.logout()

    if(user.loggedIn):
        break

    print("1. Login to existing account.")
    print("2. Register a new account.")
    print("3. Logout.")
    option = input("incorrect, re-enter option: ")

pos = "main"

while(user.loggedIn):
    if(pos == "main"):
        print("Main Menu:", "\n")
        print("1. Logout")
        print("2. Account Information")
        print("3. Inventory Information")
        print("4. Cart Information")
        
        option = "none"
        while(option[0] not in "1234"):
            option = input("Input option: ")





