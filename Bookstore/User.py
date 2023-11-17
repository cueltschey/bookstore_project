import sqlite3
import os
os.system("python3 Bookstore/Inventory.py")

class User:
    def __init__(self, database="Bookstore.db", table=""):
        self.databaseName = database
        self.tableName = table
        self.userID = ""
        self.loggedIn = False
        try:
            self.cnn = sqlite3.connect("./Bookstore/" + self.databaseName)
        except Exception as e:
            raise e 

    def login(self):
        email = input("email: ")
        password = input("password: ")
        userIDs = self.cnn.execute(f"SELECT userID FROM User WHERE Email='{email}' AND Password='{password}'")
        for u in userIDs:
            self.userID = u[0]
            print("logged in...")
            print(self.userID)
            self.loggedIn = True
            return True
        print("failed")
        return False

    def logout(self):
        self.loggedIn = False
        print("logged out...")
        return False

    def viewAccountInformation(self):
        details = self.cnn.execute(f"SELECT * FROM User WHERE UserID='{self.userID}'")
        for d in details:
            print(f"First Name: {d[3]}")
            print(f"Last Name: {d[4]}")
            return True
        print("not logged in...")
        return False

    def createAccount(self):
        email = input("Email: ")
        password = input("Password: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        add = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_user = input("Zip: ")
        payment = input("Payment: ")
        res = self.cnn.execute("INSERT INTO User VALUES (NULL,?,?,?,?,?,?,?,?,?)", (email,password,first,last,add,city,state,zip_user,payment))
        print("creating account...")

    def viewCart(self, userID, inventoryDatabase):
        # get and display books in the users cart
        items = self.cnn.execute("SELECT * FROM Cart")
        print("read")
        for item in items:
            print(item)
        

    def addToCart(userID, ISBN):
        # add a new book or increment existing book
        quantity = cnn.execute("SELECT Quantity FROM Cart WHERE ISBN='?'", ISBN)
        if(quantity):
            quantity = int(quantity)
            cnn.execute("INSERT INTO Cart VALUES (?, ?, ?)", (userID, ISBN, quantity + 1))
        else:
            cnn.execute("INSERT INTO Cart VALUES (?, ?, ?)", (userID, ISBN, 1))

    def removeFromCart(userID, ISBN):
        # remove all books of matching ISBN
        cnn.execute("REMOVE FROM Cart WHERE userID='?' AND ISBN='?'", (userID, ISBN))

    def checkOut(userID):
        # clear cart and call inventory checkout
        items = cnn.execute("SELECT * FROM Cart WHERE userID='?'", userID)
        cnn.execute("REMOVE FROM Cart WHERE userID='?'", userID)


