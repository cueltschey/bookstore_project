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
            self.cnn = sqlite3.connect("./" + self.databaseName)
        except Exception as e:
            raise e 

    def login(self):
        email = input("email: ")
        password = input("password: ")
        userID = self.cnn.execute("SELECT userID FROM User WHERE Email='?' AND Password='?'", (email, password))[0]
        if len(userID) > 0:
            print("logged in...")
            return true
        print("failed")
        return false

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


