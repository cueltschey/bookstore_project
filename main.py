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

while(option[0] not in '123' and user.loggenIn == False):
    print("1. Login to existing account.")
    print("2. Register a new account.")
    print("3. Logout.")
    option = input("incorrect, re-enter option: ")
    if(option[0] == '1'):
        user.login()
    elif(option[0] == '2'):
        user.createAccount()
    elif(option[0] == '3'):
        user.logout()

while(user.loggedIn):
    print("inside")
    break





