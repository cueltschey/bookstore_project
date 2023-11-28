from Bookstore.User import User 
from Bookstore.Inventory import Inventory
from Bookstore.Cart import Cart


user = User("Bookstore/User.db", "User")
inventory = Inventory("Bookstore/Inventory.db", "Inventory")
print("Login Page:", "\n")

print("1. Login to existing account.")
print("2. Register a new account.")
option = input("Input option here: ")

option = int(option)

while(not user.login()):
    print("Please try again...")

while(user.loggedIn):
    print("inside")
    break





