from Bookstore.User import User 
from Bookstore.Inventory import Inventory
from Bookstore.Cart import Cart


user = User("Bookstore/User.db", "User")
inventory = Inventory("Bookstore/Inventory.db", "Inventory")
print("\nLogin Page:", "\n")

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
    option = input("Enter Option: ")

pos = "main"
cart = ""
if(user.loggedIn):
    cart = Cart("Bookstore/Cart.db", "Cart")


while(user.loggedIn):
    if(pos == "main"):
        print("\nMain Menu:", "\n")
        print("1. Logout")
        print("2. Account Information")
        print("3. Inventory Information")
        print("4. Cart Information")
        
        option = "none"
        while(option not in "1234"):
            option = input("Input option: ")
        if option == "1":
            user.logout()
            break
        elif option == "2":
            user.viewAccountInformation()
        elif option == "3":
            pos = "inventory"
        else:
            pos = "cart"

    if(pos == "inventory"):
            print("\nInventory Menu:", "\n")
            print("1. Go Back")
            print("2. View Inventory")
            print("3. Search Inventory")
            
            option = "none"
            while(option not in "123"):
                option = input("Input option: ")

            if option == "1":
                pos = "main"
            elif option == "2":
                inventory.viewInventory()
            elif option == "3":
                inventory.searchInventory()
            else:
                print("Invalid option...")

    if(pos == "cart"):
            print("\nCart Menu:", "\n")
            print("1. Go Back")
            print("2. View Cart")
            print("3. Add Items")
            print("4. Remove Items")
            print("5. Checkout")
            
            option = "none"
            while(option not in "12345"):
                option = input("Input option: ")

            if option == "1":
                pos = "main"
            elif option == "2":
                cart.viewCart(user.userID)
            elif option == "3":
                ISBN = input("ISBN of book to add: ") 
                cart.addToCart(user.userID, ISBN)
            elif option == "4":
                ISBN = input("ISBN of book to remove: ")
                cart.removeFromCart(user.userID, ISBN)
            elif option == "5":
                cart.checkOut(user.userID, inventory)
            else:
                print("Invalid option...")

print("Goodbye!...")
            
